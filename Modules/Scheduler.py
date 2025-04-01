from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
import logging
from Modules.TechnicalAnalysisCalculate import calculate_sma_ema, calculate_rsi
from Modules.CryptoPanicFetcher import fetch_crypto_panic

async def scheduler_one_minutes():
    tasks = [calculate_sma_ema("technical_indicators_one_minute"), calculate_rsi("one_minute")]
    await asyncio.gather(*tasks)
    
async def scheduler_five_munutes():
    tasks = [calculate_sma_ema("technical_indicators_five_minutes"),fetch_crypto_panic("all")]
    await asyncio.gather(*tasks)

async def scheduler_fifteen_minutes():
    tasks = [fetch_crypto_panic("bullish"),fetch_crypto_panic("bearish"),calculate_sma_ema("technical_indicators_fifteen_minutes")]
    await asyncio.gather(*tasks)

async def scheduler_one_hour():
    tasks = [calculate_sma_ema("technical_indicators_one_hour"),calculate_rsi("one_hour")]
    await asyncio.gather(*tasks)

async def scheduler_four_hour():
    await calculate_sma_ema("technical_indicators_four_hours")

async def scheduler_one_day():
    tasks = [calculate_sma_ema("technical_indicators_one_day"),calculate_rsi("one_day")]
    await asyncio.gather(*tasks)

async def start_scheduler():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(scheduler_one_minutes, 'interval', minutes=1,misfire_grace_time=10)
    scheduler.add_job(scheduler_five_munutes,'interval', minutes=5,misfire_grace_time=20)
    scheduler.add_job(scheduler_fifteen_minutes,'interval', minutes=15,misfire_grace_time=30)
    scheduler.add_job(scheduler_one_hour,'interval', hours=1,misfire_grace_time=30)
    scheduler.add_job(scheduler_four_hour,'interval', hours=4,misfire_grace_time=30)
    scheduler.add_job(scheduler_one_day,'interval', days=1,misfire_grace_time=30)
    scheduler.start()






