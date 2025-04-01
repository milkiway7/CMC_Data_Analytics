import asyncio
from Modules.BinanceHistoricalDataFetcher import fetch_all_data
from Database.init_db import initialize_database
from Modules.Scheduler import start_scheduler
from logger_config import configure_logging
import logging
from Modules.CryptoPanicFetcher import fetch_crypto_panic
from Modules.BlockChain.BlockchainScheduler import blokchain_data_scheduler
from Modules.BlockChain.BlockChainDataFetcher import get_btc_blocks,get_xrp_blocks,get_eth_blocks

configure_logging()
#Entry point
async def main():
    # await initialize_database()
    # await get_btc_blocks()
    # await get_eth_blocks()
    # await get_xrp_blocks()
    try:

        logging.info('Data analysis started')

        await initialize_database()
        fetch_result = await fetch_all_data()  

        if fetch_result:  # Jeśli fetch_all_data zwróci True, uruchamiamy scheduler
            logging.info("Data fetched successfully, starting scheduler...")
            asyncio.create_task(start_scheduler())
            # asyncio.create_task(blokchain_data_scheduler())
        else:
            logging.error("Data fetching failed, scheduler will not start.")
        
        # Tworzymy Future, który nigdy się nie kończy
        await asyncio.Future()
         
    except Exception as e:
        logging.error(f"Error: Data analysis failed {e}")

if __name__ == "__main__":
    asyncio.run(main())  

