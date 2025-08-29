from aiogram import Router, types
from aiogram.filters import Command
from bot.keyboards.main_menu import main_menu_kb

router = Router()

@router.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer(
        "سلام 👋\nبه ربات حسابداری شخصی خوش اومدی!\nاز منو انتخاب کن:",
        reply_markup=main_menu_kb()
    )
