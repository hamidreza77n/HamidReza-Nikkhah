# save_tree.py
import os

def get_dir_size(path="."):
    """محاسبه حجم کل یک پوشه"""
    total = 0
    for entry in os.scandir(path):
        if entry.is_file():
            total += entry.stat().st_size
        elif entry.is_dir():
            total += get_dir_size(entry.path)
    return total

def display_tree(startpath=".", save_file="project_structure.txt"):
    with open(save_file, "w", encoding="utf-8") as f:
        for root, dirs, files in os.walk(startpath):
            level = root.replace(startpath, "").count(os.sep)
            indent = " " * 4 * level
            folder_size = get_dir_size(root)
            f.write(f"{indent}📂 {os.path.basename(root)}/ ({folder_size/1024:.2f} KB)\n")
            subindent = " " * 4 * (level + 1)
            for file in files:
                filepath = os.path.join(root, file)
                size = os.path.getsize(filepath)
                f.write(f"{subindent}📄 {file} ({size/1024:.2f} KB)\n")

    print(f"✅ ساختار پروژه در فایل {save_file} ذخیره شد.")


if __name__ == "__main__":
    # اینجا مسیر پوشه پروژه‌ات رو بده
    display_tree("AstroBot")
