from aiogram import Router, types
from aiogram.filters import Command
from bot.client import add_transaction, register_user

router = Router()

@router.message(Command("addexpense"))
async def add_expense(message: types.Message):
    await register_user(str(message.from_user.id), message.from_user.full_name)
    await message.answer("📉 مبلغ هزینه رو وارد کن:")

    @router.message()
    async def expense_amount(msg: types.Message):
        try:
            amount = float(msg.text)
            data = await add_transaction(str(msg.from_user.id), amount, "general", "expense")
            await msg.answer(f"✅ هزینه ثبت شد: {data}")
        except ValueError:
            await msg.answer("❌ لطفا یک عدد معتبر وارد کن.")

@router.message(Command("addincome"))
async def add_income(message: types.Message):
    await register_user(str(message.from_user.id), message.from_user.full_name)
    await message.answer("📈 مبلغ درآمد رو وارد کن:")

    @router.message()
    async def income_amount(msg: types.Message):
        try:
            amount = float(msg.text)
            data = await add_transaction(str(msg.from_user.id), amount, "salary", "income")
            await msg.answer(f"✅ درآمد ثبت شد: {data}")
        except ValueError:
            await msg.answer("❌ لطفا یک عدد معتبر وارد کن.")
