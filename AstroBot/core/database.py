from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import settings

# اتصال به دیتابیس
engine = create_engine(settings.DATABASE_URL, echo=False, future=True)

# ساخت Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base برای مدل‌ها
Base = declarative_base()

# Dependency برای FastAPI (در admin_web استفاده میشه)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
