import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage

from core.config import TELEGRAM_TOKEN
from core.database import get_db
from models.user_model import User

from handlers import auth_handlers, menu_handlers

logging.basicConfig(level=logging.INFO)

# Bot & Dispatcher
bot = Bot(token=TELEGRAM_TOKEN, parse_mode="HTML")
dp = Dispatcher(storage=MemoryStorage())


# --- ثبت‌نام خودکار کاربر ---
@dp.message(CommandStart())
async def start_command(message: types.Message):
    db = next(get_db())
    tg_id = str(message.from_user.id)
    username = message.from_user.username or f"user_{tg_id}"

    user = db.query(User).filter(User.telegram_id == tg_id).first()

    if not user:
        new_user = User(
            telegram_id=tg_id,
            username=username,
            is_active=False  # منتظر تأیید ادمین
        )
        db.add(new_user)
        db.commit()
        await message.answer(
            "👋 سلام!\n"
            "ثبت‌نام شما با موفقیت انجام شد ✅\n\n"
            "⏳ لطفاً منتظر تأیید ادمین باشید."
        )
    else:
        if user.is_active:
            await message.answer("✅ شما قبلاً ثبت‌نام و تأیید شدید.\n\nبرای ادامه از منو استفاده کنید.")
        else:
            await message.answer("⏳ ثبت‌نام شما در انتظار تأیید ادمین است.")


# --- ماژول‌ها (Handlers) ---
dp.include_router(auth_handlers.router)
dp.include_router(menu_handlers.router)


# --- اجرا ---
async def main():
    logging.info("🚀 Bot is running...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("❌ Bot stopped!")
