from Database.database import Database
from Database.TableModels.CandlesHistoricalData import CandlesHistoricalData
from Database.TableModels.TechnicalIndicatorsTables import TechnicalIndicators
import logging
async def initialize_database():
    db = Database()
    async with db.engine.begin() as conn:  # Używamy asynchronicznego połączenia
        await conn.run_sync(CandlesHistoricalData.metadata.create_all)
        await conn.run_sync(TechnicalIndicators.metadata.create_all)
    logging.info("Database initialized")