from Database.database import Database
from Database.TableModels.CandlesHistoricalData import CandlesHistoricalData
from sqlalchemy import select 

db = Database()

async def get_filtered_candles(symbol: str, interval: str, endtime):
    async with db.get_session() as session:
        try:
            query = select(CandlesHistoricalData).filter(
                CandlesHistoricalData.Symbol == symbol,
                CandlesHistoricalData.Interval == interval,
                CandlesHistoricalData.CloseTime > endtime
            )

            result = await session.execute(query)
            candles = result.scalars().all()

            candles_dict = []
            for candle in candles:
                candles_dict.append({
                    "symbol": candle.Symbol,
                    "interval": candle.Interval,
                    "open_time": candle.OpenTime,
                    "open": candle.Open,
                    "high": candle.High,
                    "low": candle.Low,
                    "close": candle.Close,
                    "volume": candle.Volume,
                    "close_time": candle.CloseTime
                })

            return candles_dict
        except Exception as e:
            print(f"Error - get filtered candles from db : {e}")
            return None