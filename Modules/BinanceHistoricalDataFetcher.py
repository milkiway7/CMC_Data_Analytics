import aiohttp
import asyncio
import time
from Database.save_to_db import save_candles_to_db
from Helpers.date import get_date_days_ago_ms

CANDLES_API_URL = "https://api.binance.com/api/v3/klines"
SYMBOLS = ["BTCUSDT","ETHUSDT","XRPUSDT","SOLUSDT"]
INTERVALS = ["1m", "5m", "15m", "1h"]
LIMIT = 1000

HISTORICAL_DATA_END_DATE = get_date_days_ago_ms(365,5)

async def fetch_historical_candles(symbol, interval):
    end_time = int(time.time() * 1000)  # Aktualny czas w milisekundach
    
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
                
                # Zapisanie świec do bazy danych w partiach po 1000
                await save_candles_to_db(candles)

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
    
