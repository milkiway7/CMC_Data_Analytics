import json
import aiohttp
from datetime import datetime
from Database.save_to_db import save_crypto_panic

with open("config.json","r") as file:
    config = json.load(file)


BULLISH_INFO = []
BEARISH_INFO = []
UNCLASSIFIED_INFO = []

async def fetch_crypto_panic(filter_type):

    if filter_type == "all":
        url = f"{config['CryptoPanic']['url']}?auth_token={config['CryptoPanic']['Api_Key']}&currencies=BTC,ETH,SOL,XRP"
    else:
        url = f"{config['CryptoPanic']['url']}?auth_token={config['CryptoPanic']['Api_Key']}&filter={filter_type}&currencies=BTC,ETH,SOL,XRP"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            format_data(data,filter_type)

    if(filter_type == "bullish" and BULLISH_INFO):
        await save_crypto_panic(BULLISH_INFO)
        BULLISH_INFO.clear()
    if(filter_type == "bearish" and BEARISH_INFO):
        await save_crypto_panic(BEARISH_INFO)
        BEARISH_INFO.clear()
    if(filter_type == "all" and UNCLASSIFIED_INFO):
        await save_crypto_panic(UNCLASSIFIED_INFO)
        UNCLASSIFIED_INFO.clear()

def format_data(data,filter_type):
    
    for result in data["results"]:

        date_obj = datetime.strptime(result["published_at"], '%Y-%m-%dT%H:%M:%SZ')
        timestamp_ms = int(date_obj.timestamp() * 1000)

        formatted_data = {
            "MessageId": int(result["id"]),
            "Currencies":result["currencies"][0]["code"],
            "Sentiment":filter_type,
            "PublishedAt":int(timestamp_ms),
            "Url":result["url"],
            "Title": result["title"],
            "VotesPositive": int(result["votes"]["positive"]),
            "VotesNegative": int(result["votes"]["negative"]),
            "VotesImportant": int(result["votes"]["important"])
        }

        if(filter_type == "bullish"):
            BULLISH_INFO.append(formatted_data)
        if(filter_type == "bearish"):
            BEARISH_INFO.append(formatted_data)
        if(filter_type == "all"):
            UNCLASSIFIED_INFO.append(formatted_data)
