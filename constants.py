CONSTANTS = {
    "currency" : ("BTC", "ETH", "SOL", "XRP"),
    "interval" : ("1m", "5m", "15m", "1h","4h","1d"),
    "RSI":{
        "short_term":{
            "interval": "1m",
            "period_ms": 14 * 1440 * 60000,
            "candle_count": 14 * 1440
        },
        "medium_term":{
            "interval": "1h",
            "period_ms": 14 * 24 * 60 * 60000,
            "candle_count": 14 * 24
        },
        "long_term":{
            "interval": "1d",
            "period_ms": 14 * 24 * 60 * 60000,
            "candle_count": 14 
            }
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