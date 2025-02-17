CONSTANTS = {
    "currency" : ("BTC", "ETH", "SOL", "XRP"),
    "interval" : ("1m", "5m", "15m", "1h"),
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
            "interval": "1h"
        },
        {
            "name": "Sma200",
            "period": 200,
            "interval": "1h"
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
    }
}