import asyncio
from Modules.BinanceHistoricalDataFetcher import fetch_all_data
from Database.init_db import initialize_database

#Entry point
async def main():
    initialize_database()
    candles = await fetch_all_data()  


if __name__ == "__main__":
    asyncio.run(main())  

