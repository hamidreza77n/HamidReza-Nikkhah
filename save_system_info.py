# save_project_env.py
import os
import sys
import subprocess
import platform
import json
from datetime import datetime

# کتابخانه‌های اصلی پروژه که میخوای بررسی بشن
PROJECT_LIBS = [
    "aiogram",
    "airgrom",
    "psutil",
    "requests",
    "python-dotenv",
]

def run_cmd(cmd):
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip() or result.stderr.strip()
    except Exception as e:
        return f"Error: {e}"

def get_lib_versions(libs):
    versions = {}
    for lib in libs:
        try:
            mod = __import__(lib)
            versions[lib] = getattr(mod, '__version__', 'No version attribute')
        except ImportError:
            versions[lib] = 'Not installed'
        except Exception as e:
            versions[lib] = f"Error: {e}"
    return versions

def main():
    info = {}

    # زمان و تاریخ
    info['datetime'] = str(datetime.now())

    # سیستم عامل و سخت افزار
    info['os'] = platform.platform()
    info['system'] = platform.system()
    info['release'] = platform.release()
    info['architecture'] = platform.machine()
    info['processor'] = platform.processor()
    try:
        import psutil
        info['cpu_count'] = psutil.cpu_count(logical=True)
        info['memory_total'] = psutil.virtual_memory().total
    except ImportError:
        info['cpu_count'] = 'Install psutil for CPU details'
        info['memory_total'] = 'Install psutil for RAM details'

    # Python و pip
    info['python_version'] = sys.version
    info['pip_version'] = run_cmd([sys.executable, "-m", "pip", "--version"])

    # کتابخانه‌های نصب شده
    installed_packages = run_cmd([sys.executable, "-m", "pip", "freeze"])
    info['installed_packages'] = installed_packages.splitlines()

    # نسخه کتابخانه‌های اصلی پروژه
    info['project_lib_versions'] = get_lib_versions(PROJECT_LIBS)

    # VS Code
    info['vscode_version'] = run_cmd(["code", "--version"])

    # مسیر پروژه و محیط مجازی
    info['project_path'] = os.getcwd()
    info['venv_path'] = os.environ.get("VIRTUAL_ENV", "No virtual environment detected")

    # خروجی فایل
    output_file = os.path.join(os.getcwd(), "project_env_info.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(info, f, indent=4, ensure_ascii=False)

    print(f"✅ اطلاعات پروژه و محیط توسعه ذخیره شد در: {output_file}")

if __name__ == "__main__":
    main()
