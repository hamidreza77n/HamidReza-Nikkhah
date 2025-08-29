from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

# -------------------------
# User Schemas
# -------------------------
class UserBase(BaseModel):
    telegram_id: str
    name: Optional[str] = None

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    class Config:
        orm_mode = True

# -------------------------
# Transaction Schemas
# -------------------------
class TransactionBase(BaseModel):
    amount: float
    category: str
    type: str  # income یا expense

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    id: int
    user_id: int
    date: datetime
    class Config:
        orm_mode = True

# -------------------------
# Investment Schemas
# -------------------------
class InvestmentBase(BaseModel):
    asset_type: str  # gold, silver, usd
    amount: float

class InvestmentCreate(InvestmentBase):
    pass

class InvestmentResponse(InvestmentBase):
    id: int
    user_id: int
    date: datetime
    class Config:
        orm_mode = True
