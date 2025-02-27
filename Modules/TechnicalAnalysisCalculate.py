from decimal import ROUND_HALF_UP, Decimal
import pandas as pd
from Database.get_from_db import get_filtered_candles
from Helpers.date import get_date_days_ago_ms, get_date_ago_ms
import constants
import asyncio
from Database.save_to_db import save_technical_analysis_hourly,save_technical_analysis_four_hours,save_technical_analysis_daily
import numpy as np

TECHNICAL_ANALYSIS_SHORT_TERM = {
    "BTC":{
        "SMA":{
                "Sma5" : {
                    "close_time": None,
                    "value": None,   
                },
                "Sma10" : {
                    "close_time": None,
                    "value": None
                },
                "Sma20" : {
                    "close_time": None,
                    "value": None
                }
            },
        "EMA":{
                "Ema5" : {
                    "close_time": None,
                    "value": None
                },
                "Ema10" : {
                    "close_time": None,
                    "value": None
                },                
                "Ema20" : {
                    "close_time": None,
                    "value": None
                }
            },
        },
    "ETH":{
        "SMA":{
                "Sma5" : {
                    "close_time": None,
                    "value": None,   
                },
                "Sma10" : {
                    "close_time": None,
                    "value": None
                },
                "Sma20" : {
                    "close_time": None,
                    "value": None
                }
            },
        "EMA":{
                "Ema5" : {
                    "close_time": None,
                    "value": None
                },
                "Ema10" : {
                    "close_time": None,
                    "value": None
                },                
                "Ema20" : {
                    "close_time": None,
                    "value": None
                }
            },
        },
    "SOL":{
        "SMA":{
                "Sma5" : {
                    "close_time": None,
                    "value": None,   
                },
                "Sma10" : {
                    "close_time": None,
                    "value": None
                },
                "Sma20" : {
                    "close_time": None,
                    "value": None
                }
            },
        "EMA":{
                "Ema5" : {
                    "close_time": None,
                    "value": None
                },
                "Ema10" : {
                    "close_time": None,
                    "value": None
                },                
                "Ema20" : {
                    "close_time": None,
                    "value": None
                }
            },
        },
    "XRP":{
        "SMA":{
                "Sma5" : {
                    "close_time": None,
                    "value": None,   
                },
                "Sma10" : {
                    "close_time": None,
                    "value": None
                },
                "Sma20" : {
                    "close_time": None,
                    "value": None
                }
            },
        "EMA":{
                "Ema5" : {
                    "close_time": None,
                    "value": None
                },
                "Ema10" : {
                    "close_time": None,
                    "value": None
                },                
                "Ema20" : {
                    "close_time": None,
                    "value": None
                }
            },
        }
}
TECHNICAL_ANALYSIS_MEDIUM_TERM = {
    "BTC":{
        "SMA":{
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
                }
            },
        "EMA":{
                "Ema20" : {
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
                }
            },
        },
    "ETH":{
        "SMA":{
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
                }
            },
        "EMA":{
                "Ema20" : {
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
                }
            },
        },
    "SOL":{
        "SMA":{
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
                }
            },
        "EMA":{
                "Ema20" : {
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
                }
            },
        },
    "XRP":{
        "SMA":{
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
                }
            },
        "EMA":{
                "Ema20" : {
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
                }
            },
        }
}
TECHNICAL_ANALYSIS_LONG_TERM = {
    "BTC":{
        "SMA":{
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
            }
        },
    "ETH":{
        "SMA":{
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
            }
        },
    "SOL":{
        "SMA":{
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
            }
        },
    "XRP":{
        "SMA":{
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
            }
        }
}

async def calculate_all_technical_indicators():
    tasks = [calculate_sma_ema("technical_indicators_short_term"),calculate_sma_ema("technical_indicators_medium_term"),calculate_sma_ema("technical_indicators_long_term")]
    result = await asyncio.gather(*tasks)
    if all(result):
        await calculate_macd()
    #save to db
    # await save_technical_analysis_hourly(TECHNICAL_ANALYSIS_INDICATORS_HOURLY)   
    # await save_technical_analysis_four_hours(TECHNICAL_ANALYSIS_INDICATORS_FOUR_HOURS)   
    # await save_technical_analysis_daily(TECHNICAL_ANALYSIS_INDICATORS_DAILY)
 
async def calculate_sma_ema(trading_scope):
    
    for currency in constants.CONSTANTS["currency"]:
        for technical_indicator in constants.CONSTANTS[f"{trading_scope}"]:
            
            for indicator_info in constants.CONSTANTS[f"{trading_scope}"][technical_indicator]:
                data = await get_filtered_candles(currency, indicator_info["interval"], get_date_ago_ms(indicator_info["period_ms"]),indicator_info["candle_count"])
                # SORT OLDEST TO NEWEST
                sorted_data = await sort_data_by_date(data)
                count = len(sorted_data)
                df = pd.DataFrame(sorted_data)
                
                if technical_indicator == "SMA":
                    df[indicator_info["name"]] = df["close"].rolling(window=count).mean()
                else:
                    df[indicator_info["name"]] = df["close"].ewm(span=count, adjust=False).mean()
                    
                ma_value = df[indicator_info["name"]].iloc[-1]
                
                if trading_scope == "technical_indicators_short_term":
                    TECHNICAL_ANALYSIS_SHORT_TERM[currency][f"{technical_indicator}"][indicator_info["name"]]["value"] = ma_value
                    TECHNICAL_ANALYSIS_SHORT_TERM[currency][f"{technical_indicator}"][indicator_info["name"]]["close_time"] = df["close_time"].iloc[-1]
                elif trading_scope == "technical_indicators_medium_term":
                    TECHNICAL_ANALYSIS_MEDIUM_TERM[currency][f"{technical_indicator}"][indicator_info["name"]]["value"] = ma_value
                    TECHNICAL_ANALYSIS_MEDIUM_TERM[currency][f"{technical_indicator}"][indicator_info["name"]]["close_time"] = df["close_time"].iloc[-1]
                elif trading_scope == "technical_indicators_long_term":
                    TECHNICAL_ANALYSIS_LONG_TERM[currency][f"{technical_indicator}"][indicator_info["name"]]["value"] = ma_value
                    TECHNICAL_ANALYSIS_LONG_TERM[currency][f"{technical_indicator}"][indicator_info["name"]]["close_time"] = df["close_time"].iloc[-1]
    return True
    
#oblicz raz na dzień
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
        # TECHNICAL_ANALYSIS_INDICATORS_DAILY[currency]["RSI"] = rsi
    return True

#oblicz raz na dzień  
async def calculate_macd():
    pass
    # for currency in constants.CONSTANTS["currency"]:
    #     a = TECHNICAL_ANALYSIS_INDICATORS_HOURLY[currency]["EMA"]["Ema12"]["value"]
    #     b = TECHNICAL_ANALYSIS_INDICATORS_FOUR_HOURS[currency]["EMA"]["Ema26"]["value"]
    #     TECHNICAL_ANALYSIS_INDICATORS_DAILY[currency]["MACD"] = TECHNICAL_ANALYSIS_INDICATORS_HOURLY[currency]["EMA"]["Ema12"]["value"] - TECHNICAL_ANALYSIS_INDICATORS_FOUR_HOURS[currency]["EMA"]["Ema26"]["value"]

async def sort_data_by_date(data):
    return sorted(data, key=lambda x: x["close_time"])




