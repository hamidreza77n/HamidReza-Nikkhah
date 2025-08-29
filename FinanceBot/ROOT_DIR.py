import os
import re
import shutil

# مسیر ریشه FinanceBot
ROOT_DIR = "/workspaces/HamidReza-Nikkhah/FinanceBot"

# بررسی اسم واقعی در client.py
CLIENT_FILE = os.path.join(ROOT_DIR, "bot", "client.py")
with open(CLIENT_FILE, "r", encoding="utf-8") as f:
    client_content = f.read()

# پیدا کردن نام‌های تعریف شده در client.py
defined_names = re.findall(r'^(\w+)\s*=', client_content, re.MULTILINE)
print("اسامی تعریف شده در client.py:", defined_names)

# تابع اصلاح فایل
def replace_imports(file_path):
    backup_path = file_path + ".bak"
    shutil.copy(file_path, backup_path)  # بکاپ
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # اصلاح bot_client
    content = re.sub(r'from bot\.client import bot_client', 
                     f"from bot.client import {', '.join(defined_names)}", content)

    # اصلاح backend.db.database
    content = re.sub(r'from backend\.db\.database import', 
                     'from backend.database import', content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[اصلاح شد] {file_path} (نسخه بکاپ: {backup_path})")

# گشتن در کل پروژه
for subdir, dirs, files in os.walk(ROOT_DIR):
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(subdir, file)
            replace_imports(file_path)

print("تمام ایمپورت‌ها اصلاح شدند!")
