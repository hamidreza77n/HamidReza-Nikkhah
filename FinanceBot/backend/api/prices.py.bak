from fastapi import APIRouter
from backend.services.prices import PriceService

router = APIRouter()

@router.get("/gold")
async def gold_price():
    return await PriceService.get_gold_price()

@router.get("/silver")
async def silver_price():
    return await PriceService.get_silver_price()

@router.get("/usd")
async def usd_price():
    return await PriceService.get_usd_price()
