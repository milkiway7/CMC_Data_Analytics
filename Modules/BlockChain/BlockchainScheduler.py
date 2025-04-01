from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
import logging
from Modules.BlockChain.BlockChainDataFetcher import get_assets

async def blokchain_data_scheduler():
    logging.info("Fetching assets data")
    scheduler = AsyncIOScheduler()
    scheduler.add_job(get_assets, 'interval', hours= 1, misfire_grace_time=30)
    scheduler.start()