from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🌙 وضعیت ماه"), KeyboardButton(text="🪐 چارت تولد")],
        [KeyboardButton(text="💰 قیمت‌ها"), KeyboardButton(text="🤖 چت با ChatGPT")],
        [KeyboardButton(text="🔔 نوتیفیکیشن روزانه")]
    ],
    resize_keyboard=True
)
