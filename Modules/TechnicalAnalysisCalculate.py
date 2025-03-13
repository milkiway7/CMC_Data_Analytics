from decimal import ROUND_HALF_UP, Decimal
import pandas as pd
from Database.get_from_db import get_filtered_candles
from Helpers.date import get_date_ago_ms
import constants
from Database.save_to_db import save_technical_indicators
import numpy as np

TECHNICAL_INDICATORS_SMA_EMA = []
TECHNICAL_INDICATORS_RSI = []
 
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

                TECHNICAL_INDICATORS_SMA_EMA.append({
                    "symbol": currency,
                    "interval": indicator_info["interval"],
                    "close_time": int(df["close_time"].iloc[-1]),
                    "indicator": indicator_info["name"],
                    "value": Decimal(ma_value).quantize(Decimal('0.00000001'), rounding=ROUND_HALF_UP)
                })

    await save_technical_indicators(TECHNICAL_INDICATORS_SMA_EMA)
    TECHNICAL_INDICATORS_SMA_EMA.clear()

async def calculate_rsi(technical_indicator):

    for currency in constants.CONSTANTS["currency"]:

        data = await get_filtered_candles(currency, constants.CONSTANTS["RSI"][technical_indicator]["interval"], get_date_ago_ms(constants.CONSTANTS["RSI"][technical_indicator]["period_ms"]),constants.CONSTANTS["RSI"][technical_indicator]["candle_count"])
        sorted_data = await sort_data_by_date(data)
        close_prices = [entry['close'] for entry in sorted_data]
                
        deltas = np.diff(close_prices)  
        gains = np.insert(np.where(deltas > 0, deltas, 0),0,0)  
        losses = np.insert(np.where(deltas < 0, -deltas, 0),0,0)  
            
        avg_gain = np.mean(gains[:len(gains)])  
        avg_loss =  np.mean(losses[:len(losses)])
            
        rs = None
        rsi = None
            
        if avg_loss == 0:
            rsi = 100 # avg_gain / avg_losss = 0 co znaczy że nie było spadków (maksymalnie wykupiony rynek)
        else:
            rs = avg_gain / avg_loss
            rsi = 100 - (100 / (1 + rs))
            rsi = rsi.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP) 

        TECHNICAL_INDICATORS_RSI.append({
            "symbol": currency,
            "interval": constants.CONSTANTS["RSI"][technical_indicator]["interval"],
            "close_time": sorted_data[-1]["close_time"],
            "indicator": "RSI",
            "value": rsi
        })

    await save_technical_indicators(TECHNICAL_INDICATORS_RSI)
    TECHNICAL_INDICATORS_RSI.clear()

async def sort_data_by_date(data):
    return sorted(data, key=lambda x: x["close_time"])



