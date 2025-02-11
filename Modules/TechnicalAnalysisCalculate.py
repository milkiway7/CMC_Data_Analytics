import pandas as pd
from Database.get_from_db import get_filtered_candles
from Helpers.date import get_date_days_ago_ms
import constants
import asyncio

TECHNICAL_ANALYSIS_INDICATORS = {
    "BTC":{
        "SMA":{
            "SMA_5": None,
            "SMA_10": None,
            "SMA_20": None,
            "SMA_50": None,
            "SMA_100": None,
            "SMA_200": None
            },
        "EMA":{
            "EMA_5": None,
            "EMA_9": None,
            "EMA_12": None,
            "EMA_50": None,
            "EMA_100": None,
            "EMA_200": None
            }
        },
    "ETH":{
        "SMA":{
            "SMA_5": None,
            "SMA_10": None,
            "SMA_20": None,
            "SMA_50": None,
            "SMA_100": None,
            "SMA_200": None
            },
        "EMA":{
            "EMA_5": None,
            "EMA_9": None,
            "EMA_12": None,
            "EMA_50": None,
            "EMA_100": None,
            "EMA_200": None
            }
        },
    "SOL":{
        "SMA":{
            "SMA_5": None,
            "SMA_10": None,
            "SMA_20": None,
            "SMA_50": None,
            "SMA_100": None,
            "SMA_200": None
            },
        "EMA":{
            "EMA_5": None,
            "EMA_9": None,
            "EMA_12": None,
            "EMA_50": None,
            "EMA_100": None,
            "EMA_200": None
            }
        },
    "XRP":{
        "SMA":{
            "SMA_5": None,
            "SMA_10": None,
            "SMA_20": None,
            "SMA_50": None,
            "SMA_100": None,
            "SMA_200": None
            },
        "EMA":{
            "EMA_5": None,
            "EMA_9": None,
            "EMA_12": None,
            "EMA_50": None,
            "EMA_100": None,
            "EMA_200": None
            }
        }
}

async def calculate_all_technical_indicators():
    await calculate_sma()
    # await calculate_ema()
 
#zrob dla jednego   
async def calculate_sma():
    data = await get_filtered_candles("BTC", "1h", get_date_days_ago_ms(100,1))
    # Ilość świec do określenia window dla pandas
    sorted_data = await sort_data_by_date(data)
    count = len(sorted_data)
    df = pd.DataFrame(sorted_data)
    df["sma_100"] = df["close"].rolling(window=count).mean()
    sma_serie = df["sma_100"].tolist()
    a = 1
    #save sma to db

async def calculate_ema():
    return True

async def sort_data_by_date(data):
    return sorted(data, key=lambda x: x["close_time"])


    

