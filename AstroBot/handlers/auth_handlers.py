# Auth handlers placeholder
from aiogram import Router, types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from AstroBot.core.database import SessionLocal
from AstroBot.models.user_model import User
from AstroBot.menus.main_menu import main_menu_kb
from AstroBot.config import ADMIN_TELEGRAM_ID

router = Router()

@router.message(commands=["start"])
async def start_handler(message: types.Message):
    session = SessionLocal()
    try:
        user = session.query(User).filter_by(telegram_id=str(message.from_user.id)).first()
        
        if not user:
            new_user = User(
                telegram_id=str(message.from_user.id),
                username=message.from_user.username or f"user_{message.from_user.id}",
                is_approved=False
            )
            session.add(new_user)
            session.commit()
            await message.answer("سلام! 👋 ثبت‌نام شما انجام شد.\nلطفاً منتظر تأیید ادمین باشید.")
        else:
            if not user.is_approved:
                await message.answer("👀 ثبت‌نام شما انجام شده.\nمنتظر تأیید ادمین بمانید.")
            else:
                await message.answer("✅ خوش آمدید! شما تأیید شده‌اید.", reply_markup=main_menu_kb)
    finally:
        session.close()


# 🔹 لیست کاربران در انتظار تأیید (فقط ادمین)
@router.message(commands=["pending"])
async def show_pending(message: types.Message):
    if str(message.from_user.id) != str(ADMIN_TELEGRAM_ID):
        return await message.answer("⛔ شما دسترسی ادمین ندارید.")
    
    session = SessionLocal()
    users = session.query(User).filter_by(is_approved=False).all()
    session.close()

    if not users:
        return await message.answer("✅ کاربری در انتظار تأیید وجود ندارد.")

    for user in users:
        kb = InlineKeyboardBuilder()
        kb.button(text="✅ تأیید", callback_data=f"approve_{user.id}")
        kb.button(text="❌ رد", callback_data=f"reject_{user.id}")
        await message.answer(f"👤 {user.username} (ID: {user.telegram_id})", reply_markup=kb.as_markup())


# 🔹 هندل تایید/رد
@router.callback_query(F.data.startswith("approve_"))
async def approve_user(callback: types.CallbackQuery):
    session = SessionLocal()
    user_id = int(callback.data.split("_")[1])
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        user.is_approved = True
        session.commit()
        await callback.message.edit_text(f"✅ کاربر {user.username} تأیید شد.")
        # پیام خصوصی به کاربر
        try:
            await callback.bot.send_message(user.telegram_id, "🎉 شما توسط ادمین تأیید شدید! حالا می‌توانید از منو استفاده کنید.")
        except:
            pass
    session.close()


@router.callback_query(F.data.startswith("reject_"))
async def reject_user(callback: types.CallbackQuery):
    session = SessionLocal()
    user_id = int(callback.data.split("_")[1])
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
        await callback.message.edit_text(f"❌ کاربر {user.username} رد شد و از دیتابیس حذف گردید.")
    session.close()
