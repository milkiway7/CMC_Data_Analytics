from Database.database import Database
from Database.TableModels.CandlesHistoricalData import CandlesHistoricalData
from Database.TableModels.TechnicalIndicatorsTables import TechnicalIndicatorsHourly,TechnicalIndicatorsFourHours,TechnicalIndicatorsDaily

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
            await session.commit()  
        except Exception as e:
            await session.rollback()
            print(f"Błąd zapisu do bazy: {e}")
            
async def save_technical_analysis_hourly(technical_analysis_hourly):
    async with db.get_session() as session:
        try:
            for symbol in technical_analysis_hourly:
                record = TechnicalIndicatorsHourly(Symbol=symbol)
                closeTime = 0
                for sma in technical_analysis_hourly[symbol]["SMA"]:
                    setattr(record,sma,float(technical_analysis_hourly[symbol]["SMA"][sma]["value"]))
                    if technical_analysis_hourly[symbol]["SMA"][sma]["value"] > closeTime:
                        closeTime = technical_analysis_hourly[symbol]["SMA"][sma]["close_time"]
                for ema in technical_analysis_hourly[symbol]["EMA"]:
                    setattr(record,ema,float(technical_analysis_hourly[symbol]["EMA"][ema]["value"]))
                setattr(record,"CloseTime",int(closeTime))
                session.add(record)
                await session.commit()
        except Exception as e:
            print(f"Error: can't save technical indicators SMA/EMA to database:{e}")
            await session.rollback()

async def save_technical_analysis_four_hours(technical_analysis_four_hours):
    async with db.get_session() as session:
        try:
            for symbol in technical_analysis_four_hours:
                record = TechnicalIndicatorsFourHours(Symbol=symbol)
                closeTime = 0
                for sma in technical_analysis_four_hours[symbol]["SMA"]:
                    setattr(record,sma,float(technical_analysis_four_hours[symbol]["SMA"][sma]["value"]))
                    if technical_analysis_four_hours[symbol]["SMA"][sma]["value"] > closeTime:
                        closeTime = technical_analysis_four_hours[symbol]["SMA"][sma]["close_time"]
                for ema in technical_analysis_four_hours[symbol]["EMA"]:
                    setattr(record,ema,float(technical_analysis_four_hours[symbol]["EMA"][ema]["value"]))
                setattr(record,"CloseTime",int(closeTime))
                session.add(record)
                await session.commit()
        except Exception as e:
            print(f"Error: can't save technical indicators SMA/EMA to database:{e}")
            await session.rollback()

async def save_technical_analysis_daily(technical_analysis_daily):
    async with db.get_session() as session:
        try:
            for symbol in technical_analysis_daily:
                record = TechnicalIndicatorsDaily(Symbol=symbol)
                closeTime = 0
                for sma in technical_analysis_daily[symbol]["SMA"]:
                    setattr(record,sma,float(technical_analysis_daily[symbol]["SMA"][sma]["value"]))
                    if technical_analysis_daily[symbol]["SMA"][sma]["value"] > closeTime:
                        closeTime = technical_analysis_daily[symbol]["SMA"][sma]["close_time"]
                for ema in technical_analysis_daily[symbol]["EMA"]:
                    setattr(record,ema,float(technical_analysis_daily[symbol]["EMA"][ema]["value"]))
                setattr(record,"CloseTime",int(closeTime))
                a=float(technical_analysis_daily[symbol]["RSI"])
                setattr(record,"Rsi",float(technical_analysis_daily[symbol]["RSI"]))
                setattr(record,"Macd",float(technical_analysis_daily[symbol]["MACD"]))
                session.add(record)
                await session.commit()
        except Exception as e:
            print(f"Error: can't save technical indicators SMA/EMA to database:{e}")
            await session.rollback()