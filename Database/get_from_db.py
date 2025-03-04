from Database.database import Database
from Database.TableModels.CandlesHistoricalData import Candles
from sqlalchemy import select
from datetime import datetime, timezone

db = Database()

async def get_filtered_candles(symbol: str, interval: str, endtime, num_items):
    async with db.get_session() as session:
        try:
            now = int(datetime.now(timezone.utc).timestamp() * 1000)  # Konwersja do milisekund

            # Pobranie świec w zakresie [endtime, now]
            query = select(Candles).filter(
                Candles.Symbol == symbol,
                Candles.Interval == interval,
                Candles.CloseTime.between(endtime, now)
            ).order_by(Candles.CloseTime.desc()).limit(num_items)

            result = await session.execute(query)
            candles = result.scalars().all()

            # Jeśli za mało rekordów, pobierz starsze
            if len(candles) < num_items:
                remaining = num_items - len(candles)
                older_query = select(Candles).filter(
                    Candles.Symbol == symbol,
                    Candles.Interval == interval,
                    Candles.CloseTime < endtime
                ).order_by(Candles.CloseTime.desc()).limit(remaining)

                older_result = await session.execute(older_query)
                older_candles = older_result.scalars().all()
                candles.extend(older_candles)

            candles_dict = [
                {
                    "symbol": candle.Symbol,
                    "interval": candle.Interval,
                    "open_time": candle.OpenTime,
                    "open": candle.Open,
                    "high": candle.High,
                    "low": candle.Low,
                    "close": candle.Close,
                    "volume": candle.Volume,
                    "close_time": candle.CloseTime
                }
                for candle in candles
            ]

            return candles_dict

        except Exception as e:
            print(f"Error - get filtered candles from db: {e}")
            return None
