import aiohttp
import json
import logging
import constants
import asyncio
from Database.save_to_db import save_assets_info
with open("config.json","r") as file:
    config = json.load(file)

async def fetch_data(session, url):
    headers = {
        'x-api-key': config['CryptoApi']['Api_Key'],  
        'Content-Type': 'application/json', 
    }
    async with session.get(url, headers=headers) as response:
        if response.status == 200:
            try:
                
                return await response.json()
            except Exception as e:
                logging.error(f"Error decoding JSON: {e}")
                
                text = await response.text()
                logging.error(f"Response text: {text}")
                return None
        else:
            logging.error(f"Error: {response.status}, URL: {url}")
            text = await response.text()
            logging.error(f"Error response: {text}")
            return None 

async def get_assets():
    for symbol in constants.CONSTANTS['currency']:
        url= f"{config['CryptoApi']['url']}/market-data/assets/by-symbol/{symbol}?context=assetsInfo"
        async with aiohttp.ClientSession() as session:
            data = await fetch_data(session, url)
            # save data to db
            await save_assets_info(data)
        await asyncio.sleep(5)
    
async def get_btc_blocks():
    url = f"{config['CryptoApi']['url']}/blocks/utxo/bitcoin/mainnet/latest/unspent-outputs?context=BTC&count=2"
    async with aiohttp.ClientSession() as session:
        data = await fetch_data(session, url)
        # save data to db
        a =1 

async def get_eth_blocks():
    url = f"{config['CryptoApi']['url']}/blocks/evm/ethereum/mainnet/latest?context=ETH&count=50"
    async with aiohttp.ClientSession() as session:
        data = await fetch_data(session, url)
        # save data to db
        a =1 

async def get_xrp_blocks():
    url = f"{config['CryptoApi']['url']}/blocks/xrp/mainnet/latest?context=XRP&count=50"
    async with aiohttp.ClientSession() as session:
        data = await fetch_data(session, url)
        # save data to db
        a =1 