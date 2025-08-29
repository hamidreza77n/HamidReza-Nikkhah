# bot/client.py
from aiogram import Bot, Dispatcher

# تنظیمات کلاینت
BACKEND_URL = "http://localhost:8000"
API_KEY = "your_api_key_here"
DEFAULT_HEADERS = {}

# نمونه Dispatcher و Bot
bot_instance = Bot(token="YOUR_TELEGRAM_BOT_TOKEN")
bot_client = Dispatcher(bot_instance)
