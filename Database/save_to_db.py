from sqlalchemy.future import select
from Database.database import Database
from Database.TableModels.CandlesHistoricalData import Candles
from Database.TableModels.TechnicalIndicatorsTables import TechnicalIndicators
from Database.TableModels.CryptoPanicTable import CryptoPanicTable
import logging

db = Database()
async def save_crypto_panic(data):
    try:
        batch_size = 20
        async with db.get_session() as session:

            info_ids = {str(record["MessageId"]) for record in data}  # Używamy set() zamiast listy, żeby uniknąć duplikatów

            if not info_ids:
                return 
            
            result = await session.execute(select(CryptoPanicTable.MessageId).filter(CryptoPanicTable.MessageId.in_(info_ids)))
            existing_info_ids = {row[0] for row in result.fetchall()}  # Zbieramy istniejące MessageId do setu

            # Filtruj dane, aby zostawić tylko te, które nie są duplikatami
            unique_data = [record for record in data if record["MessageId"] not in existing_info_ids]

            # Jeśli mamy jakieś unikalne dane, zapisz je w bazie

            if unique_data:
                for i in range(0, len(unique_data), batch_size):
                    batch = unique_data[i:i + batch_size]
                    session.add_all([CryptoPanicTable(**record) for record in batch])
                    await session.commit()

    except Exception as e:
        logging.info(f"DATABASE ERROR: saving crypto panic data {e}")

async def save_candles_to_db(candles_data):
    try:
        batch_size = 100  # Możesz dostosować rozmiar partii
        async with db.get_session() as session:
            for i in range(0, len(candles_data), batch_size):
                batch = candles_data[i:i + batch_size]
                session.add_all([Candles(**candle) for candle in batch])
                await session.commit()
    except Exception as e:
        logging.info(f"DATABASE ERROR: saving candle data {e}")
            
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
