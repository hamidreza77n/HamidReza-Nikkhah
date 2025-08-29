from fastapi import APIRouter, Depends
from aiogram import Bot
from aiogram.types import Message
from database import get_db, User
from sqlalchemy.orm import Session

auth_router = APIRouter()

@auth_router.post("/register")
async def register_user(user_id: int, username: str, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.telegram_id == user_id).first()
    if existing_user:
        return {"status": "already_registered"}
    
    new_user = User(telegram_id=user_id, username=username, is_approved=False)
    db.add(new_user)
    db.commit()
    
    # پیام خوش آمدگویی به کاربر
    bot = Bot(token="YOUR_BOT_TOKEN")
    await bot.send_message(chat_id=user_id, text="سلام! 👋 لطفاً منتظر تأیید ادمین بمانید.")
    
    # پیام به ادمین
    admin_id = 7124090618
    await bot.send_message(chat_id=admin_id,
                           text=f"کاربر جدید ثبت‌نام کرد:\nUsername: {username}\nTelegram ID: {user_id}")
    
    return {"status": "registered"}
