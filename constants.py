CONSTANTS = {
    "currency" : ("BTC", "ETH", "SOL", "XRP"),
    "interval" : ("1m", "5m", "15m", "1h","4h","1d"),
    "SMA" : [
        {
            "name": "Sma5",
            "period": 5,
            "interval": "1m"
        },
        {
            "name": "Sma10",
            "period": 10,
            "interval": "5m",
        },
        {
            "name": "Sma20",
            "period": 20,
            "interval": "15m",
        },
        {
            "name": "Sma50",
            "period": 50,
            "interval": "1h"
        },
        {
            "name": "Sma100",
            "period": 100,
            "interval": "4h"
        },
        {
            "name": "Sma200",
            "period": 200,
            "interval": "1d"
        }
    ],
    "EMA" : [
        {
            "name": "Ema5",
            "period": 5,
            "interval": "1m"
        },
        {
            "name": "Ema9",
            "period": 9,
            "interval": "5m",
        },
        {
            "name": "Ema12",
            "period": 12,
            "interval": "15m",
        },
        {
            "name": "Ema26",
            "period": 26,
            "interval": "1h"
        },
        {
            "name": "Ema100",
            "period": 100,
            "interval": "1h"
        },
        {
            "name": "Ema200",
            "period": 200,
            "interval": "1h"
        }
    ],
    "RSI":{
        "period": 14,
        "interval": "1d"
    },
    "technical_indicators_short_term":{
        "SMA":[
            {
            "name": "Sma5",
            "candle_count": 5,
            "period_ms": 5 * 60000,
            "interval": "1m"
            },
            {
            "name": "Sma10",
            "candle_count": 10,
            "period_ms": 10 * 5 * 60000,
            "interval": "5m",
            },
            {
            "name": "Sma20",
            "candle_count": 20,
            "period_ms": 20 * 15 * 60000,
            "interval": "15m",
            }
        ],
        "EMA":[
            {
            "name": "Ema5",
            "candle_count": 5,
            "period_ms": 5 * 60000,
            "interval": "1m"
            },
            {
            "name": "Ema10",
            "candle_count": 10,
            "period_ms": 10 * 5 * 60000,
            "interval": "5m",
            },
            {
            "name": "Ema20",
            "candle_count": 20,
            "period_ms": 20 * 15 * 60000,
            "interval": "15m",
            }
        ]
    },
    "technical_indicators_medium_term":{
        "SMA":[
            {
            "name": "Sma20",
            "candle_count": 20,
            "period_ms": 20 * 60 * 60000,
            "interval": "1h"
            },
            {
            "name": "Sma50",
            "candle_count": 50,
            "period_ms": 50 * 4 * 60 * 60000,
            "interval": "4h"
            },
            {
            "name": "Sma100",
            "candle_count": 100,
            "period_ms": 100 * 1440 * 60000,
            "interval": "1d",
            }
        ],
        "EMA":[
            {
            "name": "Ema20",
            "candle_count": 20,
            "period_ms": 20 * 60 * 60000,
            "interval": "1h"
            },
            {
            "name": "Ema50",
            "candle_count": 50,
            "period_ms": 50 * 4 * 60 * 60000,
            "interval": "4h",
            },
            {
            "name": "Ema100",
            "candle_count": 100,
            "period_ms": 100 * 1440 * 60000,
            "interval": "1d",
            }
        ]
    },
    "technical_indicators_long_term":{
        "SMA":[
            {
            "name": "Sma50",
            "candle_count": 50,
            "period_ms": 50 * 1440 * 60000,
            "interval": "1d"
            },            
            {
            "name": "Sma100",
            "candle_count": 100,
            "period_ms": 100 * 1440 * 60000,
            "interval": "1d"
            },            
            {
            "name": "Sma200",
            "candle_count": 200,
            "period_ms": 200 * 1440 * 60000,
            "interval": "1d"
            }
        ],
        "EMA":[
            {
            "name": "Ema50",
            "candle_count": 50,
            "period_ms": 50 * 1440 * 60000,
            "interval": "1d"
            },
            {
            "name": "Ema100",
            "candle_count": 100,
            "period_ms": 100 * 1440 * 60000,
            "interval": "1d"
            },
            {
            "name": "Ema200",
            "candle_count": 200,
            "period_ms": 200 * 1440 * 60000,
            "interval": "1d"
            }
        ]
    }
}