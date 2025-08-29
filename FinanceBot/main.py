import sys
import os

# اضافه کردن مسیر ریشه پروژه به PYTHONPATH
root_path = os.path.dirname(os.path.abspath(__file__))
if root_path not in sys.path:
    sys.path.append(root_path)

# import پکیج‌های backend
from backend.database import create_session, get_engine
from backend.config import settings

def main():
    print("Backend is running...")
    # اینجا می‌توانی FastAPI app یا سایر سرویس‌ها را اجرا کنی
    # uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()
