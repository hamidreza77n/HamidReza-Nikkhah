#!/bin/bash
# مسیر ربات
BOT_PATH="/workspaces/HamidReza-Nikkhah/AstroBot"
VENV_PATH="/workspaces/HamidReza-Nikkhah/.venv"
SESSION_NAME="astrobot"

# فعال کردن virtualenv
source "$VENV_PATH/bin/activate"

# بررسی session tmux
tmux has-session -t $SESSION_NAME 2>/dev/null
if [ $? -eq 0 ]; then
    echo "❌ Session $SESSION_NAME قبلا فعال بود. می‌بندیم..."
    tmux kill-session -t $SESSION_NAME
fi

# ساخت و اجرای tmux جدید
echo "🚀 اجرای ربات در session: $SESSION_NAME"
tmux new-session -d -s $SESSION_NAME "$VENV_PATH/bin/python $BOT_PATH/bot_ai.py"
echo "✅ ربات داخل tmux اجرا شد."
echo "👉 برای مشاهده لاگ: tmux attach -t $SESSION_NAME"
