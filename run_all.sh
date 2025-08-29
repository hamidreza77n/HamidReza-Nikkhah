#!/bin/bash

# فعال کردن محیط مجازی
source /workspaces/HamidReza-Nikkhah/.venv/bin/activate

# رفتن به مسیر پروژه
cd /workspaces/HamidReza-Nikkhah/FinanceBot

# ست کردن PYTHONPATH برای شناسایی ماژول‌ها
export PYTHONPATH=$(pwd)

# ایجاد پوشه لاگ در صورت نبودن
mkdir -p logs

# اجرای ربات تلگرام در background با ذخیره لاگ
echo "Starting Telegram Bot..."
nohup python -m bot.main > logs/telegram_bot.log 2>&1 &

# اجرای وب اپلیکیشن FastAPI
echo "Starting Web App..."
nohup python -m uvicorn web_app.main:app --reload --host 0.0.0.0 --port 8000 > logs/web_app.log 2>&1 &
