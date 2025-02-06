import asyncio
from Modules.BinanceHistoricalDataFetcher import fetch_all_data


#Entry point
async def main():
    candles = await fetch_all_data()  


if __name__ == "__main__":
    asyncio.run(main())  

