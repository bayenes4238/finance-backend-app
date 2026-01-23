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
            p = t.fast_info["lastPrice"]
            c = t.fast_info["lastPrice"] / t.fast_info["previousClose"] * 100 - 100
            out[key] = {
                "p": round(p, 2),
                "c": round(c, 2)
            }
        except:
            out[key] = {"p": 0, "c": 0}
    return out

data = {
    "stocks": {
        "bist": fetch_group(BIST),
        "us": fetch_group(US)
    },
    "ts": int(time.time())
}

with open("data.json", "w") as f:
    json.dump(data, f)
