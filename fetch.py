import yfinance as yf
import json
import time

BIST = {
    "THYAO": "THYAO.IS",
    "ASELS": "ASELS.IS",
    "KCHOL": "KCHOL.IS"
}

US = {
    "AAPL": "AAPL",
    "MSFT": "MSFT",
    "TSLA": "TSLA"
}

def fetch_group(group):
    out = {}
    for key, symbol in group.items():
        try:
            t = yf.Ticker(symbol)
            info = t.fast_info

            last = info.get("lastPrice")
            prev = info.get("previousClose")

            if last is None or prev is None:
                raise Exception("No price data")

            change = (last / prev - 1) * 100

            out[key] = {
                "p": round(last, 2),
                "c": round(change, 2)
            }

            print(f"OK {key}: {last}")

        except Exception as e:
            print(f"ERR {key}: {e}")
            out[key] = {
                "p": 0,
                "c": 0
            }
    return out

data = {
    "usdtry": 0,   # burayı sonra bağlarız
    "coin": [
        { "name": "BTC", "price": 0 },
        { "name": "ETH", "price": 0 }
    ],
    "stocks": {
        "bist": fetch_group(BIST),
        "us": fetch_group(US)
    },
    "status": "ok",
    "ts": int(time.time()),
    "debug": int(time.time())
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

print("JSON WRITTEN AT", data["ts"])
