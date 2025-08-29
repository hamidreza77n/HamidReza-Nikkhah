# backend/api/transactions.py
from fastapi import APIRouter, UploadFile, File, Form, HTTPException, Depends
from fastapi.responses import JSONResponse
import os
from typing import Optional
from backend.database import AsyncSessionLocal, engine, Base  # اصلاح شد
from backend.crud.transactions import create_transaction, get_summary_by_user, get_transactions_by_user
from backend.models.models import Transaction
from sqlalchemy.orm import Session
from datetime import datetime

router = APIRouter()

# اطمینان از ایجاد جداول
Base.metadata.create_all(bind=engine)

UPLOAD_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static", "uploads", "receipts")
os.makedirs(UPLOAD_DIR, exist_ok=True)

# تابع دریافت session
def get_db():
    db = AsyncSessionLocal()  # اصلاح نام به AsyncSessionLocal
    try:
        yield db
    finally:
        db.close()

@router.post("/create")
async def api_create_transaction(
    user_id: int = Form(...),
    type: str = Form(...),
    amount: float = Form(...),
    category: Optional[str] = Form(None),
    description: Optional[str] = Form(None),
    receipt: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db),
):
    receipt_path = None
    if receipt is not None:
        # ذخیره فایل
        filename = f"{int(datetime.utcnow().timestamp())}_{receipt.filename}"
        file_path = os.path.join(UPLOAD_DIR, filename)
        with open(file_path, "wb") as f:
            f.write(await receipt.read())
        receipt_path = f"/static/uploads/receipts/{filename}"

    tx = create_transaction(
        db=db,
        user_id=user_id,
        type_=type,
        amount=amount,
        category=category or "سایر",
        description=description,
        receipt=receipt_path
    )
    return JSONResponse({"status": "ok", "transaction_id": tx.id, "receipt_path": receipt_path})

@router.get("/summary/{user_id}")
def api_summary(user_id: int, db: Session = Depends(get_db)):
    summary = get_summary_by_user(db, user_id)
    return summary

@router.get("/list/{user_id}")
def api_list(user_id: int, limit: int = 20, db: Session = Depends(get_db)):
    items = get_transactions_by_user(db, user_id, limit)
    result = []
    for t in items:
        result.append({
            "id": t.id,
            "type": t.type,
            "amount": t.amount,
            "category": t.category,
            "description": t.description,
            "receipt_path": t.receipt_path,
            "created_at": t.created_at.isoformat()
        })
    return result

@router.get("/chart/{user_id}")
def api_chart(user_id: int, db: Session = Depends(get_db)):
    items = db.query(Transaction).filter(Transaction.user_id == user_id).all()
    from collections import defaultdict
    data_income = defaultdict(float)
    data_expense = defaultdict(float)
    for t in items:
        day = t.created_at.date().isoformat()
        if t.type == "income":
            data_income[day] += t.amount
        else:
            data_expense[day] += t.amount
    all_days = sorted(set(list(data_income.keys()) + list(data_expense.keys())))
    chart = {
        "labels": all_days,
        "income": [data_income.get(d, 0) for d in all_days],
        "expense": [data_expense.get(d, 0) for d in all_days],
    }
    return chart
