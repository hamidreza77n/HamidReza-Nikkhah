# web_app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# فقط ماژول‌های موجود import شده‌اند
from backend.services import prices  # investments و transactions هنوز موجود نیستند

app = FastAPI(title="FinanceBot Web API")

# پیکربندی CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # در صورت نیاز محدود کنید
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "FinanceBot Web App is running."}

# نمونه endpoint برای prices
@app.get("/prices")
async def get_prices():
    data = await prices.get_prices()  # فرض بر این است که تابع async get_prices در prices.py وجود دارد
    return {"prices": data}
