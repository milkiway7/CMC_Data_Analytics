import asyncio
from Modules.BinanceHistoricalDataFetcher import fetch_all_data
from Database.init_db import initialize_database
from Modules.Scheduler import start_scheduler
from logger_config import configure_logging
import logging
from Modules.CryptoPanicFetcher import fetch_crypto_panic

configure_logging()
#Entry point
async def main():
    try:

        logging.info('Data analysis started')

        await initialize_database()
        fetch_result = await fetch_all_data()  

        if fetch_result:  # Jeśli fetch_all_data zwróci True, uruchamiamy scheduler
            asyncio.create_task(start_scheduler())
        else:
            logging.error("Data fetching failed, scheduler will not start.")
        
        # Tworzymy Future, który nigdy się nie kończy
        await asyncio.Future()
         
    except Exception as e:
        logging.error(f"Error: Data analysis failed {e}")

if __name__ == "__main__":
    asyncio.run(main())  

