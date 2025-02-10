import pandas as pd

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

def calculate_sma_ema(data):
    if data[0]["symbol"] == "BTC" and data[0]["interval"] == "1h":
        intems_count = len(data)
        unique_symbols = set(data[0]["symbol"] for candle in data)
        unique_intervals = set(data[0]["interval"] for candle in data)
        len_item = len(data[0])
        len_item1 = len(data[1])
        len_item2= len(data[2])
        len_item3 = len(data[3])
        close0= data[0]["close_time"]
        close3= data[3]["close_time"]
        
        min_close_time_entry = min(data, key=lambda x: x['close_time'])
        a =0