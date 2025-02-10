import aiohttp
import asyncio
import time
from Database.save_to_db import save_candles_to_db
from datetime import datetime, timedelta, timezone
from Modules.TechnicalAnalysisCalculate import calculate_sma_ema
CANDLES_API_URL = "https://api.binance.com/api/v3/klines"
SYMBOLS = ["BTCUSDT","ETHUSDT","XRPUSDT","SOLUSDT"]
INTERVALS = ["1m", "5m", "15m", "1h"]
LIMIT = 1000

def get_date_ago_ms(days_number, product):
    date_seven_years_ago = datetime.now(timezone.utc) - timedelta(days=days_number*product)
    date_miliseconds = int(date_seven_years_ago.timestamp() * 1000)
    return date_miliseconds

HISTORICAL_DATA_END_DATE = get_date_ago_ms(365,5)
DATE_TECHNICAL_INDICATOR_10 = get_date_ago_ms(10,1)
DATE_TECHNICAL_INDICATOR_20 = get_date_ago_ms(20,1)
DATE_TECHNICAL_INDICATOR_50 = get_date_ago_ms(50,1)
DATE_TECHNICAL_INDICATOR_200 = get_date_ago_ms(200,1)

async def fetch_historical_candles(symbol, interval):
    end_time = int(time.time() * 1000)  # Aktualny czas w milisekundach
    data_technical_indicators = []
    
    async with aiohttp.ClientSession() as session:
        while True:
            url = f"{CANDLES_API_URL}?symbol={symbol}&interval={interval}&limit={LIMIT}&endTime={end_time}"
            async with session.get(url) as response:
                if response.status != 200:
                    print(f"Błąd dla {symbol} {interval}: {response.status}")
                    break

                data = await response.json()

                if not data:
                    print(f"Brak starszych danych dla {symbol} {interval}")
                    break  # Koniec historii

                # Przetwarzanie świec i dodanie symbolu oraz interwału
                candles = [
                    {
                        "symbol": symbol[:3],
                        "interval": interval,
                        "open_time": candle[0],
                        "open": candle[1],
                        "high": candle[2],
                        "low": candle[3],
                        "close": candle[4],
                        "volume": candle[5],
                        "close_time": candle[6],
                    }
                    for candle in data
                ]

                match interval:
                    case "1m":
                        #sprawdzenie czy nie została przekroczona data
                        if candles[0]["close_time"] > DATE_TECHNICAL_INDICATOR_10:
                            #dodaj do listy
                            data_technical_indicators.extend(candles)
                        return True
                    case "5m":
                        if candles[0]["close_time"] > DATE_TECHNICAL_INDICATOR_20:
                            data_technical_indicators.extend(candles)
                    case "15m":
                        if candles[0]["close_time"] > DATE_TECHNICAL_INDICATOR_50:
                            data_technical_indicators.extend(candles)
                    case "1h":
                        if candles[0]["close_time"] > DATE_TECHNICAL_INDICATOR_200:
                            data_technical_indicators.extend(candles)
                            
                if end_time < DATE_TECHNICAL_INDICATOR_200:
                    #send to technical anaylsis calculate method
                    calculate_sma_ema(data_technical_indicators)
                
                # Zapisanie świec do bazy danych w partiach po 1000
                # await save_candles_to_db(candles)

                # Sprawdzenie, czy pobraliśmy mniej niż limit (koniec danych)
                if len(data) < LIMIT:
                    print(f"Osiągnięto początek historii dla {symbol} {interval}")
                    break

                # Ustaw nowy endTime jako najstarszy czas - 1ms (żeby uniknąć duplikatów)
                end_time = data[0][0] - 1

                if end_time < HISTORICAL_DATA_END_DATE:
                    print(f"Osiągnięto maksymalną datę historii dla {symbol} {interval}")
                    break

async def fetch_all_data():
    tasks = [fetch_historical_candles(symbol, interval) for symbol in SYMBOLS for interval in INTERVALS]
    await asyncio.gather(*tasks)
    
