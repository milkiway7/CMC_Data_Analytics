import asyncio
from Modules.BinanceHistoricalDataFetcher import fetch_all_data
from Database.init_db import initialize_database
from Modules.TechnicalAnalysisCalculate import calculate_all_technical_indicators
from logger_config import configure_logging
import logging

configure_logging()
#Entry point
async def main():
    try:

        logging.info('Data analysis started')
        await initialize_database()
        # await fetch_all_data()  
        await calculate_all_technical_indicators()

    except Exception as e:
        logging.error(f"Error: Data analysis failed {e}")

if __name__ == "__main__":
    asyncio.run(main())  

