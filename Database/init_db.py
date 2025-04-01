from Database.database import Database
from Database.TableModels.CandlesHistoricalData import Candles
from Database.TableModels.TechnicalIndicatorsTables import TechnicalIndicators
from Database.TableModels.CryptoPanicTable import CryptoPanicTable
from Database.TableModels.AssetsInfoFromBlockchain import AssetsInfoFromBlockchain
from Database.TableModels.BlocksInfoTable import BlocksInfoTable

import logging

async def initialize_database():
    db = Database()
    async with db.engine.begin() as conn:  # Używamy asynchronicznego połączenia
        await conn.run_sync(Candles.metadata.create_all)
        await conn.run_sync(TechnicalIndicators.metadata.create_all)
        await conn.run_sync(CryptoPanicTable.metadata.create_all)
        await conn.run_sync(AssetsInfoFromBlockchain.metadata.create_all)
        await conn.run_sync(BlocksInfoTable.metadata.create_all)
    logging.info("Database initialized")