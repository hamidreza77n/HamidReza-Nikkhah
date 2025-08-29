#!/bin/bash
# ---------------------------------------------
# Run FinanceBot Project (Bot + Backend)
# ---------------------------------------------

# مسیر پروژه
ROOT_DIR="$(dirname "$(realpath "$0")")"
echo "مسیر پروژه: $ROOT_DIR"

# تنظیم PYTHONPATH به مسیر FinanceBot
export PYTHONPATH="$ROOT_DIR"
echo "PYTHONPATH تنظیم شد: $PYTHONPATH"

# اجرای backend
echo "در حال اجرای backend..."
python -m backend.main &
BACKEND_PID=$!
echo "Backend PID=$BACKEND_PID"

# اجرای bot
echo "در حال اجرای ربات..."
python -m bot.main &
BOT_PID=$!
echo "ربات PID=$BOT_PID"

# صبر کردن تا Ctrl+C
trap "echo 'در حال توقف...'; kill $BACKEND_PID $BOT_PID; exit" SIGINT SIGTERM
wait $BACKEND_PID $BOT_PID
