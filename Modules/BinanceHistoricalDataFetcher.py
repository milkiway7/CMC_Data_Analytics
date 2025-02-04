import aiohttp
import asyncio


CANDLES_API_URL = "https://api.binance.com/api/v3/klines"
SYMBOLS = ["BTCUSDT","ETHUSDT","XRPUSDT","SOLUSDT"]
INTERVALS = ["1m","5m","15m","1h"]
LIMIT = 3

# Funkcja asynchroniczna do pobierania świec (klines)
async def fetch_historical_candles(symbol, interval):
    url = f"{CANDLES_API_URL}?symbol={symbol}&interval={interval}&limit={LIMIT}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                print(f"Błąd przy pobieraniu danych dla {symbol} {interval}: {response.status}")
                return None
                

# Funkcja do iterowania po wszystkich symbolach i interwałach
async def fetch_all_data():
    tasks = []
    for symbol in SYMBOLS:
        for interval in INTERVALS:
            tasks.append(fetch_historical_candles(symbol, interval))    # Uruchamiamy wszystkie zadania równolegle
    results = await asyncio.gather(*tasks)
    return results