import asyncio
from Modules.BinanceHistoricalDataFetcher import fetch_all_data
from Database.init_db import initialize_database

from Modules.TechnicalAnalysisCalculate import calculate_all_technical_indicators


#Entry point
async def main():
    await initialize_database()
    # await calculate_all_technical_indicators()
    await fetch_all_data()  


if __name__ == "__main__":
    asyncio.run(main())  

