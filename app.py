import asyncio
from Modules.BinanceHistoricalDataFetcher import fetch_all_data
from Database.init_db import initialize_database
from Modules.TechnicalAnalysisCalculate import start_scheduler
from logger_config import configure_logging
import logging

configure_logging()
#Entry point
async def main():
    try:

        logging.info('Data analysis started')
        await initialize_database()
        start_scheduler()

        # fetch_result = await fetch_all_data()  
        # if fetch_result:  # Jeśli fetch_all_data zwróci True, uruchamiamy scheduler
        #     logging.info("Data fetched successfully, starting scheduler...")
        #     start_scheduler()
        # else:
        #     logging.error("Data fetching failed, scheduler will not start.")

    except Exception as e:
        logging.error(f"Error: Data analysis failed {e}")

if __name__ == "__main__":
    asyncio.run(main())  

