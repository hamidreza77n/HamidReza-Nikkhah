# backend/crud/transactions.py
from sqlalchemy.orm import Session
from backend.models.models import Transaction

def create_transaction(db: Session, user_id: int, type_: str, amount: float, category: str, description: str = None, receipt: str = None):
    transaction = Transaction(
        user_id=user_id,
        type=type_,
        amount=amount,
        category=category,
        description=description,
        receipt_path=receipt
    )
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction

def get_transactions_by_user(db: Session, user_id: int, limit: int = 10):
    return db.query(Transaction).filter(Transaction.user_id == user_id).order_by(Transaction.created_at.desc()).limit(limit).all()

def get_summary_by_user(db: Session, user_id: int):
    income = db.query(Transaction).filter(Transaction.user_id == user_id, Transaction.type == "income").all()
    expense = db.query(Transaction).filter(Transaction.user_id == user_id, Transaction.type == "expense").all()
    total_income = sum(t.amount for t in income)
    total_expense = sum(t.amount for t in expense)
    balance = total_income - total_expense
    return {"income": total_income, "expense": total_expense, "balance": balance}
