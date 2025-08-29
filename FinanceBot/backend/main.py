from fastapi import FastAPI
from backend.api import prices, transactions  # فایل‌های API

app = FastAPI(title="FinanceBot Backend")

# Include routers
app.include_router(prices.router)
app.include_router(transactions.router)

# ایجاد دیتابیس
from backend.database import engine, Base
import asyncio

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(init_db())
