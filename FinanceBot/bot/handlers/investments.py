from aiogram import Router, types
from aiogram.filters import Command
from bot.client import add_investment, register_user

router = Router()

@router.message(Command("addinvestment"))
async def add_investment_cmd(message: types.Message):
    await register_user(str(message.from_user.id), message.from_user.full_name)
    await message.answer("💰 لطفا به این فرمت وارد کن:\n\nمثال:\n`gold 100`")

    @router.message()
    async def investment_input(msg: types.Message):
        try:
            asset_type, amount = msg.text.split()
            data = await add_investment(str(msg.from_user.id), asset_type.lower(), float(amount))
            await msg.answer(f"✅ سرمایه‌گذاری ثبت شد: {data}")
        except Exception as e:
            await msg.answer(f"❌ ورودی معتبر نیست. مثال: `silver 50` \n ({e})")
