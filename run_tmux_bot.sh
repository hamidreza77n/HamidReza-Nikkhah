#!/bin/bash

# نام session
SESSION_NAME="AstroBot"

# مسیر پروژه رو بذار اینجا
PROJECT_PATH="/workspaces/HamidReza-Nikkhah"

# بررسی می‌کنه session قبلاً ساخته نشده باشه
tmux has-session -t $SESSION_NAME 2>/dev/null

if [ $? != 0 ]; then
    echo "ساختن session جدید tmux و اجرای ربات..."
    tmux new-session -d -s $SESSION_NAME -n bot "cd $PROJECT_PATH && python -m AstroBot.bot_ai"
    echo "Session '$SESSION_NAME' ساخته شد و ربات در حال اجراست."
else
    echo "Session '$SESSION_NAME' قبلاً وجود داره. متصل می‌شویم..."
fi

# اتصال به session
tmux attach -t $SESSION_NAME
