import aiohttp
import asyncio
import time

CANDLES_API_URL = "https://api.binance.com/api/v3/klines"
SYMBOLS = ["BTCUSDT"]
INTERVALS = ["1m", "5m", "15m", "1h"]
LIMIT = 1000

# Funkcja asynchroniczna do pobierania świec (klines)
async def fetch_historical_candles(symbol, interval):
    end_time = int(time.time() * 1000)  # Aktualny czas w milisekundach
    all_data = []

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
                        "symbol": symbol,
                        "interval": interval,
                        "open_time": candle[0],
                        "open": candle[1],
                        "high": candle[2],
                        "low": candle[3],
                        "close": candle[4],
                        "volume": candle[5],
                        "end_time": candle[6],
                    }
                    for candle in data
                ]

                all_data.extend(candles)

                # Sprawdzenie, czy pobraliśmy mniej niż limit (koniec danych)
                if len(data) < LIMIT:
                    print(f"Osiągnięto początek historii dla {symbol} {interval}")
                    break

                # Ustaw nowy endTime jako najstarszy czas - 1ms (żeby uniknąć duplikatów)
                end_time = data[0][0] - 1

    return all_data

# Funkcja do iterowania po wszystkich symbolach i interwałach
async def fetch_all_data():
    tasks = [fetch_historical_candles(symbol, interval) for symbol in SYMBOLS for interval in INTERVALS]
    results = await asyncio.gather(*tasks)
    
    # Flatten list of lists (ponieważ gather zwraca listę list)
    return [item for sublist in results for item in sublist]
