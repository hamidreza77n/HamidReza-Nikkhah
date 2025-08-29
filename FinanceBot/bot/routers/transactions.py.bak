# bot/routers/transactions.py
import re
import os
import aiofiles
from aiogram import Router, types
from aiogram.filters import Command
from bot.client import create_transaction_api
from tempfile import NamedTemporaryFile

router = Router()

# helper: save incoming photo to temp file and return path
async def save_photo_to_temp(file: types.PhotoSize, bot) -> str:
    file_info = await bot.get_file(file.file_id)
    # create a temp filename in project (or use NamedTemporaryFile)
    tmp = NamedTemporaryFile(delete=False, suffix=".jpg", prefix="receipt_")
    tmp_path = tmp.name
    tmp.close()
    await bot.download_file(file_info.file_path, tmp_path)
    return tmp_path

# flow: user sends /درآمد amount description? optionally photo afterwards
@router.message(Command("درآمد"))
async def income_command(message: types.Message):
    parts = message.text.split(maxsplit=2)
    if len(parts) < 2:
        await message.answer("فرمت: /درآمد <مبلغ> [توضیح]. مثال: /درآمد 6000000 حقوق")
        return
    try:
        amount = float(parts[1])
    except:
        await message.answer("لطفا مقدار عددی معتبر وارد کنید.")
        return
    description = parts[2] if len(parts) >= 3 else ""
    # ask if user wants to attach receipt
    await message.answer("اگر رسید دارید یک عکس ارسال کنید؛ در غیر این صورت /nok را ارسال کنید.")

    # wait for next message from same user (simple ephemeral handler)
    @router.message()
    async def after_income(msg: types.Message):
        # ignore if msg is command or from other user
        if msg.from_user.id != message.from_user.id:
            return
        # user cancelled with /nok
        if msg.text and msg.text.strip() == "/nok":
            res = await create_transaction_api(user_id=message.from_user.id, type_="income", amount=amount, category=None, description=description)
            await msg.answer(f"✅ درآمد ثبت شد.\n{res}")
            return
        # if photo
        if msg.photo:
            # take largest photo
            photo = msg.photo[-1]
            tmp_path = await save_photo_to_temp(photo, router.bot)
            res = await create_transaction_api(user_id=message.from_user.id, type_="income", amount=amount, category=None, description=description, receipt_file_path=tmp_path)
            # cleanup tmp file
            try:
                os.remove(tmp_path)
            except:
                pass
            await msg.answer(f"✅ درآمد ثبت شد.\n{res}")
            return
        # otherwise treat it as cancel or not understood
        await msg.answer("ورودی نامعتبر؛ اگر نمی‌خواهید رسید ارسال کنید /nok را ارسال کنید.")

# flow for expense
@router.message(Command("هزینه"))
async def expense_command(message: types.Message):
    parts = message.text.split(maxsplit=2)
    if len(parts) < 2:
        await message.answer("فرمت: /هزینه <مبلغ> [توضیح]. مثال: /هزینه 150000 تاکسی")
        return
    try:
        amount = float(parts[1])
    except:
        await message.answer("لطفا مقدار عددی معتبر وارد کنید.")
        return
    description = parts[2] if len(parts) >= 3 else ""
    await message.answer("اگر رسید دارید یک عکس ارسال کنید؛ در غیر این صورت /nok را ارسال کنید.")

    @router.message()
    async def after_expense(msg: types.Message):
        if msg.from_user.id != message.from_user.id:
            return
        if msg.text and msg.text.strip() == "/nok":
            res = await create_transaction_api(user_id=message.from_user.id, type_="expense", amount=amount, category=None, description=description)
            await msg.answer(f"✅ هزینه ثبت شد.\n{res}")
            return
        if msg.photo:
            photo = msg.photo[-1]
            tmp_path = await save_photo_to_temp(photo, router.bot)
            res = await create_transaction_api(user_id=message.from_user.id, type_="expense", amount=amount, category=None, description=description, receipt_file_path=tmp_path)
            try:
                os.remove(tmp_path)
            except:
                pass
            await msg.answer(f"✅ هزینه ثبت شد.\n{res}")
            return
        await msg.answer("ورودی نامعتبر؛ اگر نمی‌خواهید رسید ارسال کنید /nok را ارسال کنید.")
