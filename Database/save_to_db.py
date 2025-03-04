from Database.database import Database
from Database.TableModels.CandlesHistoricalData import Candles
from Database.TableModels.TechnicalIndicatorsTables import TechnicalIndicators
import logging

db = Database()

async def save_candles_to_db(candles_data):
    try:
        batch_size = 100  # Możesz dostosować rozmiar partii
        async with db.get_session() as session:
            for i in range(0, len(candles_data), batch_size):
                batch = candles_data[i:i + batch_size]
                session.add_all([Candles(**candle) for candle in batch])
                await session.commit()
    except Exception as e:
        logging.info(f"Database write error: {e}")
            
async def save_technical_indicators(technical_analysis_data):
    async with db.get_session() as session:
        try:
            for data in technical_analysis_data:
                record = TechnicalIndicators(
                    Symbol=data["symbol"],
                    CloseTime=data["close_time"],
                    Indicator=data["indicator"],
                    Interval=data["interval"],
                    Value=data["value"]
                )
                session.add(record)
            await session.commit()
        except Exception as e:
            logging.info(f"Database write error: {e}")
            await session.rollback()
