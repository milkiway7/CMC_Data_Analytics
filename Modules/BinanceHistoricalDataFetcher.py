import aiohttp
import asyncio
import time
from Database.save_to_db import save_candles_to_db, get_lastes_candle
from Helpers.date import get_date_days_ago_ms

CANDLES_API_URL = "https://api.binance.com/api/v3/klines"
SYMBOLS = ["BTCUSDT","ETHUSDT","XRPUSDT","SOLUSDT"]
INTERVALS = ["1m", "5m", "15m","30m","1h","4h","1d"]
LIMIT = 1000

def calculate_end_date_per_interval(interval):
    match interval:
        case "1m":
            return get_date_days_ago_ms(365,1)
        case "5m":
            return get_date_days_ago_ms(365,1)
        case "15m":
            return get_date_days_ago_ms(365,1)
        case "30m":
            return get_date_days_ago_ms(365,3)
        case "1h":
            return get_date_days_ago_ms(365,3)
        case "4h":
            return get_date_days_ago_ms(365,3)
        case "1d":
            return get_date_days_ago_ms(365,7)

async def fetch_historical_candles(symbol, interval):
    fetch_from_data = int(time.time() * 1000)  # Aktualny czas w milisekundach
    lastest_candle = await get_lastes_candle(symbol[:3], interval)
    Historical_data_end_date = calculate_end_date_per_interval(interval)
    async with aiohttp.ClientSession() as session:
        while True:
            url = f"{CANDLES_API_URL}?symbol={symbol}&interval={interval}&limit={LIMIT}&endTime={fetch_from_data}"

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
                        "Symbol": symbol[:3],
                        "Interval": interval,
                        "OpenTime": candle[0],
                        "Open": candle[1],
                        "High": candle[2],
                        "Low": candle[3],
                        "Close": candle[4],
                        "Volume": candle[5],
                        "CloseTime": candle[6]
                    }
                    for candle in data
                ]
                
                if lastest_candle is not None:
                    if lastest_candle.CloseTime > candles[0]["CloseTime"]:
                        print(f"Pobrano brakujące świece dla {symbol} {interval}")
                        break

                # Zapisanie świec do bazy danych w partiach po 1000
                await save_candles_to_db(candles)

                # Ustaw nowy endTime jako najstarszy czas - 1ms (żeby uniknąć duplikatów)
                fetch_from_data = data[0][0] - 1
                
                if fetch_from_data < Historical_data_end_date:
                    print(f"Osiągnięto maksymalną datę historii dla {symbol} {interval}")
                    break

async def fetch_all_data():
    try:
        tasks = [fetch_historical_candles(symbol, interval) for symbol in SYMBOLS for interval in INTERVALS]
        await asyncio.gather(*tasks)
        return True  
    except Exception as e:
        print(f"Error while fetching data: {e}")
        return False  