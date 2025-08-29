#!/bin/bash
SESSION_NAME="astrobot"
VENV_PATH="/workspaces/HamidReza-Nikkhah/.venv"
BOT_PATH="/workspaces/HamidReza-Nikkhah/AstroBot/bot_ai.py"

echo "🛑 بستن همه پروسه‌های قدیمی bot_ai.py ..."
pkill -f "bot_ai.py" 2>/dev/null

echo "🛑 بستن سشن قدیمی tmux (اگر هست)..."
tmux kill-session -t $SESSION_NAME 2>/dev/null

echo "🚀 اجرای ربات در tmux (سشن: $SESSION_NAME) ..."
tmux new-session -d -s $SESSION_NAME "source $VENV_PATH/bin/activate && python $BOT_PATH"

echo "✅ ربات فقط یکبار اجرا شد (داخل tmux)."
echo "👉 برای مشاهده لاگ: lb"
