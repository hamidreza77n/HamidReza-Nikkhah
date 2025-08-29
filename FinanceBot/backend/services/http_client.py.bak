import aiohttp
import os

API_KEY = os.getenv("API_KEY", "Bv5S3LchsVyjETfmAvvnrAzdBpqlMlvL")

DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/127.0.0.1 Safari/537.36"
    ),
    "Authorization": f"Bearer {API_KEY}"
}

class HttpClient:
    """کلاس مرکزی برای درخواست‌های HTTP با User-Agent معتبر"""

    @staticmethod
    async def get(url: str, params: dict = None):
        async with aiohttp.ClientSession(headers=DEFAULT_HEADERS) as session:
            async with session.get(url, params=params) as resp:
                return await resp.json()

    @staticmethod
    async def post(url: str, data: dict = None):
        async with aiohttp.ClientSession(headers=DEFAULT_HEADERS) as session:
            async with session.post(url, json=data) as resp:
                return await resp.json()
