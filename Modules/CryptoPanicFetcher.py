import json

import aiohttp

with open("config.json","r") as file:
    config = json.load(file)

async def fetch_crypto_panic(filter_type="bullish"):

    url = f"{config["CryptoPanic"]["url"]}?auth_token={config["CryptoPanic"]["Api_Key"]}&filter={filter_type}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data