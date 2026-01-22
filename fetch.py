import requests
import json

def get_usdtry():
    url = "https://open.er-api.com/v6/latest/USD"
    r = requests.get(url, timeout=10)
    data = r.json()
    return float(data["rates"]["TRY"])

def get_crypto(symbol):
    url = f"https://min-api.cryptocompare.com/data/price?fsym={symbol}&tsyms=USD"
    r = requests.get(url, timeout=10)
    data = r.json()
    return float(data["USD"])

def main():
    usdtry = get_usdtry()

    btc_usd = get_crypto("BTC")
    eth_usd = get_crypto("ETH")

    data = {
        "usdtry": round(usdtry, 4),
        "coin": [
            {"name": "BTC", "price": round(btc_usd * usdtry, 0)},
            {"name": "ETH", "price": round(eth_usd * usdtry, 0)}
        ],
        "status": "ok"
    }

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("data.json başarıyla güncellendi")

if __name__ == "__main__":
    main()
