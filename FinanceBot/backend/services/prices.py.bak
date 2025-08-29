from .http_client import HttpClient

class PriceService:
    BASE_URL = "https://api.example.com"  # آدرس API خارجی

    @staticmethod
    async def get_gold_price():
        url = f"{PriceService.BASE_URL}/gold"
        return await HttpClient.get(url)

    @staticmethod
    async def get_silver_price():
        url = f"{PriceService.BASE_URL}/silver"
        return await HttpClient.get(url)

    @staticmethod
    async def get_usd_price():
        url = f"{PriceService.BASE_URL}/usd"
        return await HttpClient.get(url)
