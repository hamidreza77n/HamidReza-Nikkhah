import os
from dotenv import load_dotenv

# بارگذاری فایل .env
load_dotenv()

class Settings:
    TELEGRAM_TOKEN: str = os.getenv("TELEGRAM_TOKEN", "")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./finance.db")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecret")
    DEBUG: bool = os.getenv("DEBUG", "True").lower() in ("true", "1")

settings = Settings()
