from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from backend.config import settings
from backend.models import Base, User, Transaction, Investment

# اتصال دیتابیس
engine = create_async_engine(settings.DATABASE_URL, echo=settings.DEBUG, future=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

# -------------------------
# CRUD Functions
# -------------------------

# ایجاد دیتابیس
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# User
async def create_user(db: AsyncSession, telegram_id: str, name: str = None):
    user = User(telegram_id=telegram_id, name=name)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

async def get_user_by_telegram_id(db: AsyncSession, telegram_id: str):
    result = await db.execute(
        User.__table__.select().where(User.telegram_id == telegram_id)
    )
    return result.scalar_one_or_none()

# Transaction
async def add_transaction(db: AsyncSession, user_id: int, amount: float, category: str, type: str):
    tx = Transaction(user_id=user_id, amount=amount, category=category, type=type)
    db.add(tx)
    await db.commit()
    await db.refresh(tx)
    return tx

# Investment
async def add_investment(db: AsyncSession, user_id: int, asset_type: str, amount: float):
    inv = Investment(user_id=user_id, asset_type=asset_type, amount=amount)
    db.add(inv)
    await db.commit()
    await db.refresh(inv)
    return inv
