from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

# ایمپورت‌های اصلاح‌شده
from FinanceBot.backend.models import Transaction
from FinanceBot.backend.database import AsyncSessionLocal

router = Router()


@router.message(Command("درآمد"))
async def add_income(message: Message):
    parts = message.text.split()
    if len(parts) < 3:
        await message.answer("❌ فرمت درست: /درآمد مبلغ توضیح")
        return
    amount = float(parts[1])
    description = " ".join(parts[2:])

    async with AsyncSessionLocal() as session:
        txn = Transaction(amount=amount, type="income", description=description)
        session.add(txn)
        await session.commit()
    await message.answer(f"✅ درآمد {amount} ثبت شد.")


@router.message(Command("هزینه"))
async def add_expense(message: Message):
    parts = message.text.split()
    if len(parts) < 3:
        await message.answer("❌ فرمت درست: /هزینه مبلغ توضیح")
        return
    amount = float(parts[1])
    description = " ".join(parts[2:])

    async with AsyncSessionLocal() as session:
        txn = Transaction(amount=amount, type="expense", description=description)
        session.add(txn)
        await session.commit()
    await message.answer(f"✅ هزینه {amount} ثبت شد.")
