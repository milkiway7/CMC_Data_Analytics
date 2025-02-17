from decimal import ROUND_HALF_UP, Decimal
import pandas as pd
from Database.get_from_db import get_filtered_candles
from Helpers.date import get_date_days_ago_ms
import constants
import asyncio
from Database.save_to_db import save_technical_analysis_to_db
import numpy as np

TECHNICAL_ANALYSIS_INDICATORS = {
    "BTC":{
        "RSI":None,
        "MACD": None,
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
                "Ema26" : {
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
        "RSI":None,
        "MACD": None,
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
                "Ema26" : {
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
        "RSI":None,
        "MACD": None,
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
                "Ema26" : {
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
        "RSI":None,
        "MACD": None,
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
                "Ema26" : {
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
    tasks = [calculate_sma_ema_macd(),calculate_rsi()]
    await asyncio.gather(*tasks)
    #save to db
    await save_technical_analysis_to_db(TECHNICAL_ANALYSIS_INDICATORS)   

#zrob dla jednego   
async def calculate_sma_ema_macd():
    
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
    
        TECHNICAL_ANALYSIS_INDICATORS[currency]["MACD"] = TECHNICAL_ANALYSIS_INDICATORS[currency]["EMA"]["Ema12"]["value"] - TECHNICAL_ANALYSIS_INDICATORS[currency]["EMA"]["Ema26"]["value"]

async def calculate_rsi():
    
    for currency in constants.CONSTANTS["currency"]:
        data = await get_filtered_candles(currency,constants.CONSTANTS["RSI"]["interval"],get_date_days_ago_ms(constants.CONSTANTS["RSI"]["period"],1))
        sorted_data = await sort_data_by_date(data)
        close_prices = [entry['close'] for entry in sorted_data]
        
        if len(close_prices) > 14:
            close_prices = close_prices[-14:]
            
        deltas = np.diff(close_prices)  # Różnice między kolejnymi dniami
        gains = np.insert(np.where(deltas > 0, deltas, 0),0,0)  # Tylko wzrosty
        losses = np.insert(np.where(deltas < 0, -deltas, 0),0,0)  # Tylko spadki (wartości dodatnie)
        
        avg_gain = np.mean(gains[:len(gains)])  # Tablica na średnie wzrosty
        avg_loss =  np.mean(losses[:len(losses)])
        
        rs = None
        rsi = None
        
        if avg_loss == 0:
            rsi = 100 # avg_gain / avg_losss = 0 co znaczy że nie było spadków (maksymalnie wykupiony rynek)
        else:
            rs = avg_gain / avg_loss
            rsi = 100 - (100 / (1 + rs))
            rsi = rsi.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP) 
        
        TECHNICAL_ANALYSIS_INDICATORS[currency]["RSI"] = rsi
        
async def sort_data_by_date(data):
    return sorted(data, key=lambda x: x["close_time"])




