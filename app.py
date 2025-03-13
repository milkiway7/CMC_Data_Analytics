import asyncio
from Modules.BinanceHistoricalDataFetcher import fetch_all_data
from Database.init_db import initialize_database
from Modules.SchedulerTechnicalIndicators import start_scheduler
from logger_config import configure_logging
import logging
from Modules.CryptoPanicFetcher import fetch_crypto_panic

configure_logging()
#Entry point
async def main():
    try:

        logging.info('Data analysis started')
        await initialize_database()
        # fetch_result = await fetch_all_data()  
        asyncio.create_task(start_scheduler())

        a = 1
        while True:
            a += 1
            print(a)
            await asyncio.sleep(5)
        # Tworzymy Future, który nigdy się nie kończy
        await asyncio.Future() 
        # if fetch_result:  # Jeśli fetch_all_data zwróci True, uruchamiamy scheduler

        #     asyncio.gather(scheduler_one_minute())
        #     result = await fetch_crypto_panic()
        # else:
        #     logging.error("Data fetching failed, scheduler will not start.")
        a = 1
    except Exception as e:
        logging.error(f"Error: Data analysis failed {e}")

if __name__ == "__main__":
    asyncio.run(main())  

