import requests
import json

def get_usdtry():
    url = "https://open.er-api.com/v6/latest/USD"
    r = requests.get(url, timeout=10)
    data = r.json()
    return float(data["rates"]["TRY"])

def get_binance(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    r = requests.get(url, timeout=10)
    data = r.json()
    return float(data["price"])

def main():
    usdtry = get_usdtry()

    btc_usd = get_binance("BTCUSDT")
    eth_usd = get_binance("ETHUSDT")

    btc_try = btc_usd * usdtry
    eth_try = eth_usd * usdtry

    data = {
        "usdtry": round(usdtry, 4),
        "coin": [
            {"name": "BTC", "price": round(btc_try, 0)},
            {"name": "ETH", "price": round(eth_try, 0)}
        ]
    }

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("data.json başarıyla güncellendi")

if __name__ == "__main__":
    main()
