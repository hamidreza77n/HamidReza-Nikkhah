from aiogram import Router, types
from AstroBot.menus.main_menu import main_menu_kb

router = Router()

@router.message(commands=["menu"])
async def show_menu(message: types.Message):
    await message.answer("📌 منوی اصلی:", reply_markup=main_menu_kb)
