from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("➕ تراکنش جدید", callback_data="add_transaction"),
        InlineKeyboardButton("📊 گزارش سریع", callback_data="quick_report")
    )
    keyboard.add(
        InlineKeyboardButton("⏰ یادآوری‌ها", callback_data="reminders"),
        InlineKeyboardButton("💰 سرمایه‌گذاری", callback_data="investments")
    )
    keyboard.add(
        InlineKeyboardButton("⚙️ تنظیمات کاربر", callback_data="settings")
    )
    return keyboard
