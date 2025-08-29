from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.services import async_session, create_user, get_user_by_telegram_id, add_transaction, add_investment
from backend.schemas import UserCreate, UserResponse, TransactionCreate, TransactionResponse, InvestmentCreate, InvestmentResponse

router = APIRouter()

# Dependency برای session
async def get_db():
    async with async_session() as session:
        yield session

# -------------------------
# User Routes
# -------------------------
@router.post("/users/", response_model=UserResponse)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await get_user_by_telegram_id(db, user.telegram_id)
    if db_user:
        return db_user
    return await create_user(db, telegram_id=user.telegram_id, name=user.name)

# -------------------------
# Transaction Routes
# -------------------------
@router.post("/transactions/", response_model=TransactionResponse)
async def create_transaction(tx: TransactionCreate, db: AsyncSession = Depends(get_db)):
    # برای سادگی فرض می‌کنیم کاربر اول موجود هست (بعداً auth اضافه می‌کنیم)
    user = await get_user_by_telegram_id(db, "test_user")
    if not user:
        user = await create_user(db, "test_user", "Test User")
    return await add_transaction(db, user.id, tx.amount, tx.category, tx.type)

# -------------------------
# Investment Routes
# -------------------------
@router.post("/investments/", response_model=InvestmentResponse)
async def create_investment(inv: InvestmentCreate, db: AsyncSession = Depends(get_db)):
    user = await get_user_by_telegram_id(db, "test_user")
    if not user:
        user = await create_user(db, "test_user", "Test User")
    return await add_investment(db, user.id, inv.asset_type, inv.amount)
