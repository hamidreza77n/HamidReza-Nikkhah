from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from backend.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    type = Column(String, index=True)  # income / expense
    amount = Column(Float)
    category = Column(String, index=True)
    description = Column(String, nullable=True)
    receipt_path = Column(String, nullable=True)  # آدرس فایل رسید
    created_at = Column(DateTime, default=datetime.utcnow)
