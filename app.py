import asyncio
from Modules.BinanceHistoricalDataFetcher import fetch_all_data


# Funkcja główna, w której wywołasz FetchHistoricalCandles
async def main():
    candles = await fetch_all_data()  # Wywołanie funkcji asynchronicznej
    print(candles)  # Wydrukuj dane

# Uruchomienie programu
if __name__ == "__main__":
    asyncio.run(main())  # Uruchom funkcję main() w pętli eventowej
