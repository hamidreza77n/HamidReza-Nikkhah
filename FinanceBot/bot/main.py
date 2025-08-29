# bot/main.py
import asyncio
from bot.client import bot_client
from bot.routers.user import user_router  # حتما router ها وجود داشته باشند
from bot.routers.transactions import transactions_router

async def main():
    # اضافه کردن router ها به Dispatcher
    bot_client.include_router(user_router)
    bot_client.include_router(transactions_router)
    print("ربات در حال اجراست...")
    await bot_client.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
