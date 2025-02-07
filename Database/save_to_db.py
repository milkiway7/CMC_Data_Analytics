from Database.database import Database
from Database.TableModels.CandlesHistoricalData import CandlesHistoricalData

db = Database()

async def save_candles_to_db(candles_data):
    async with db.get_session() as session:  # Używamy asynchronicznego kontekstu
        try:
            for candle in candles_data:
                record = CandlesHistoricalData(
                    Symbol=candle["symbol"],
                    Interval=candle["interval"],
                    OpenTime=candle["open_time"],
                    Open=candle["open"],
                    High=candle["high"],
                    Low=candle["low"],
                    Close=candle["close"],
                    Volume=candle["volume"],
                    CloseTime=candle["close_time"]
                )
                session.add(record)
            
            # Czekamy na zakończenie commit
            await session.commit()  # Asynchroniczny commit
        except Exception as e:
            await session.rollback()
            print(f"Błąd zapisu do bazy: {e}")
