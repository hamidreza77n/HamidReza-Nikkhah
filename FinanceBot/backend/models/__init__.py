from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

# جدول کاربران
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=True)

    transactions = relationship("Transaction", back_populates="user")
    investments = relationship("Investment", back_populates="user")

# جدول تراکنش‌ها (هزینه/درآمد)
class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)  # مثلا غذا، حقوق، ...
    type = Column(String, nullable=False)  # income یا expense
    date = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="transactions")

# جدول سرمایه‌گذاری‌ها
class Investment(Base):
    __tablename__ = "investments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    asset_type = Column(String, nullable=False)  # gold, silver, usd
    amount = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="investments")
