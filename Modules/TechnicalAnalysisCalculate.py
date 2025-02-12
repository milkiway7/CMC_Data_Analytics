import pandas as pd
from Database.get_from_db import get_filtered_candles
from Helpers.date import get_date_days_ago_ms
import constants
import asyncio
from Database.save_to_db import save_technical_analysis_to_db
TECHNICAL_ANALYSIS_INDICATORS = {
    "BTC":{
        "SMA":{
                "Sma5" : {
                    "close_time": None,
                    "value": None
                },
                "Sma10" : {
                    "close_time": None,
                    "value": None
                },                
                "Sma20" : {
                    "close_time": None,
                    "value": None
                },                
                "Sma50" : {
                    "close_time": None,
                    "value": None
                },                
                "Sma100" : {
                    "close_time": None,
                    "value": None
                },                
                "Sma200" : {
                    "close_time": None,
                    "value": None
                }
            },
        "EMA":{
                "Ema5" : {
                    "close_time": None,
                    "value": None
                },
                "Ema9" : {
                    "close_time": None,
                    "value": None
                },                
                "Ema12" : {
                    "close_time": None,
                    "value": None
                },                
                "Ema50" : {
                    "close_time": None,
                    "value": None
                },                
                "Ema100" : {
                    "close_time": None,
                    "value": None
                },                
                "Ema200" : {
                    "close_time": None,
                    "value": None
                }
            },
        },
    "ETH":{
        "SMA":{
                "Sma5" : {
                    "close_time": None,
                    "value": None
                },
                "Sma10" : {
                    "close_time": None,
                    "value": None
                },                
                "Sma20" : {
                    "close_time": None,
                    "value": None
                },                
                "Sma50" : {
                    "close_time": None,
                    "value": None
                },                
                "Sma100" : {
                    "close_time": None,
                    "value": None
                },                
                "Sma200" : {
                    "close_time": None,
                    "value": None
                }
            },
        "EMA":{
                "Ema5" : {
                    "close_time": None,
                    "value": None
                },
                "Ema9" : {
                    "close_time": None,
                    "value": None
                },                
                "Ema12" : {
                    "close_time": None,
                    "value": None
                },                
                "Ema50" : {
                    "close_time": None,
                    "value": None
                },                
                "Ema100" : {
                    "close_time": None,
                    "value": None
                },                
                "Ema200" : {
                    "close_time": None,
                    "value": None
                }
            },
        },
    "SOL":{
        "SMA":{
                "Sma5" : {
                    "close_time": None,
                    "value": None
                },
                "Sma10" : {
                    "close_time": None,
                    "value": None
                },                
                "Sma20" : {
                    "close_time": None,
                    "value": None
                },                
                "Sma50" : {
                    "close_time": None,
                    "value": None
                },                
                "Sma100" : {
                    "close_time": None,
                    "value": None
                },                
                "Sma200" : {
                    "close_time": None,
                    "value": None
                }
            },
        "EMA":{
                "Ema5" : {
                    "close_time": None,
                    "value": None
                },
                "Ema9" : {
                    "close_time": None,
                    "value": None
                },                
                "Ema12" : {
                    "close_time": None,
                    "value": None
                },                
                "Ema50" : {
                    "close_time": None,
                    "value": None
                },                
                "Ema100" : {
                    "close_time": None,
                    "value": None
                },                
                "Ema200" : {
                    "close_time": None,
                    "value": None
                }
            },
        },
    "XRP":{
        "SMA":{
                "Sma5" : {
                    "close_time": None,
                    "value": None
                },
                "Sma10" : {
                    "close_time": None,
                    "value": None
                },                
                "Sma20" : {
                    "close_time": None,
                    "value": None
                },                
                "Sma50" : {
                    "close_time": None,
                    "value": None
                },                
                "Sma100" : {
                    "close_time": None,
                    "value": None
                },                
                "Sma200" : {
                    "close_time": None,
                    "value": None
                }
            },
        "EMA":{
                "Ema5" : {
                    "close_time": None,
                    "value": None
                },
                "Ema9" : {
                    "close_time": None,
                    "value": None
                },                
                "Ema12" : {
                    "close_time": None,
                    "value": None
                },                
                "Ema50" : {
                    "close_time": None,
                    "value": None
                },                
                "Ema100" : {
                    "close_time": None,
                    "value": None
                },                
                "Ema200" : {
                    "close_time": None,
                    "value": None
                }
            },
        }
}

async def calculate_all_technical_indicators():
    tasks = [calculate_sma_ema()]
    await asyncio.gather(*tasks)
    #save to db
    for symbol in TECHNICAL_ANALYSIS_INDICATORS:
        print(symbol)
        for sma in TECHNICAL_ANALYSIS_INDICATORS[symbol]["SMA"]:
            print(sma)
            print(TECHNICAL_ANALYSIS_INDICATORS[symbol]["SMA"][sma]["value"])
            print(TECHNICAL_ANALYSIS_INDICATORS[symbol]["SMA"][sma]["close_time"])
    await save_technical_analysis_to_db(TECHNICAL_ANALYSIS_INDICATORS)   
    
 
#zrob dla jednego   
async def calculate_sma_ema():
    
    for currency in constants.CONSTANTS["currency"]:
        for sma_data in constants.CONSTANTS["SMA"]:
            
            data = await get_filtered_candles(currency, sma_data["interval"], get_date_days_ago_ms(sma_data["period"],1))
            sorted_data = await sort_data_by_date(data)
            count = len(sorted_data)
            df = pd.DataFrame(sorted_data)
            df[sma_data["name"]] = df["close"].rolling(window=count).mean()
            sma_value = df[sma_data["name"]].iloc[-1]
            
            TECHNICAL_ANALYSIS_INDICATORS[currency]["SMA"][sma_data["name"]]["value"] = sma_value
            TECHNICAL_ANALYSIS_INDICATORS[currency]["SMA"][sma_data["name"]]["close_time"] = df["close_time"].iloc[-1]
            
        
            for ema_data in constants.CONSTANTS["EMA"]:
                data = await get_filtered_candles(currency, ema_data["interval"], get_date_days_ago_ms(ema_data["period"],1))
                sorted_data = await sort_data_by_date(data)
                count = len(sorted_data)
                df = pd.DataFrame(sorted_data)
                df[ema_data["name"]] = df["close"].ewm(span=count, adjust=False).mean()
                ema_value = df[ema_data["name"]].iloc[-1]
                
                TECHNICAL_ANALYSIS_INDICATORS[currency]["EMA"][ema_data["name"]]["value"] = ema_value
                TECHNICAL_ANALYSIS_INDICATORS[currency]["EMA"][ema_data["name"]]["close_time"] = df["close_time"].iloc[-1] 

async def sort_data_by_date(data):
    return sorted(data, key=lambda x: x["close_time"])


    

