from Database.database import Database
from Database.TableModels.CandlesHistoricalData import CandlesHistoricalData
from Database.TableModels.TechnicalIndicatorsTable import TechnicalIndicatorsTable

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
            
async def save_technical_analysis_to_db(technical_analysis_data):
    async with db.get_session() as session:
        try:
            for symbol in technical_analysis_data:
                record = TechnicalIndicatorsTable(
                    Symbol=symbol, 
                    Rsi = float(technical_analysis_data[symbol]["RSI"]))
                
                for sma in technical_analysis_data[symbol]["SMA"]:
                    
                    if(sma == "Sma5"):
                        setattr(record,"CloseTime",int(technical_analysis_data[symbol]["SMA"][sma]["close_time"])), 
                        
                    setattr(record,sma,float(technical_analysis_data[symbol]["SMA"][sma]["value"]))
                    
                for ema in technical_analysis_data[symbol]["EMA"]:
                    setattr(record,ema,float(technical_analysis_data[symbol]["EMA"][ema]["value"]))
                
                session.add(record)
                await session.commit()
        except Exception as e:
            print(f"Error: can't save technical indicators SMA/EMA to database:{e}")
            await session.rollback()