import os

# مسیر پوشه FinanceBot را مشخص کنید
root_dir = os.path.join(os.getcwd(), "FinanceBot")

# مسیر فایل خروجی
output_file = os.path.join(os.getcwd(), "FinanceBot_structure.txt")

def tree(dir_path, prefix=""):
    lines = []
    entries = sorted(os.listdir(dir_path))
    for i, entry in enumerate(entries):
        path = os.path.join(dir_path, entry)
        connector = "└── " if i == len(entries) - 1 else "├── "
        lines.append(f"{prefix}{connector}{entry}")
        if os.path.isdir(path):
            extension = "    " if i == len(entries) - 1 else "│   "
            lines.extend(tree(path, prefix + extension))
    return lines

if os.path.exists(root_dir):
    tree_lines = tree(root_dir)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(tree_lines))
    print(f"ساختار پوشه و فایل‌ها در {output_file} ذخیره شد.")
else:
    print(f"پوشه {root_dir} وجود ندارد.")
