import requests
import json

def get_usdtry():
    try:
        url = "https://api.exchangerate.host/latest?base=USD&symbols=TRY"
        r = requests.get(url, timeout=10)
        data = r.json()

        if "rates" in data and "TRY" in data["rates"]:
            return float(data["rates"]["TRY"])
        else:
            print("USDTRY API cevap beklenmedik:", data)
            return 30.0  # fallback
    except Exception as e:
        print("USDTRY hata:", e)
        return 30.0  # fallback

def get_coin(id):
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={id}&vs_currencies=usd"
        r = requests.get(url, timeout=10)
        data = r.json()
        return float(data[id]["usd"])
    except Exception as e:
        print(f"{id} hata:", e)
        return 0.0

def main():
    usdtry = get_usdtry()

    btc = get_coin("bitcoin")
    eth = get_coin("ethereum")

    # Altın & Gümüş (ons USD)
    gold_ons = get_coin("gold")
    silver_ons = get_coin("silver")

    gold_gram = (gold_ons * usdtry) / 31.1035
    silver_gram = (silver_ons * usdtry) / 31.1035

    data = {
        "coin": [
            {"name": "BTC", "price": round(btc, 2)},
            {"name": "ETH", "price": round(eth, 2)},
            {"name": "USDT", "price": "Üzerinde çalışılıyor"},
            {"name": "XRP", "price": "Üzerinde çalışılıyor"}
        ],
        "bist": [
            {"name": "THYAO", "price": "Üzerinde çalışılıyor"},
            {"name": "KTLEV", "price": "Üzerinde çalışılıyor"}
        ],
        "us": [
            {"name": "NVDA", "price": "Üzerinde çalışılıyor"},
            {"name": "TSLA", "price": "Üzerinde çalışılıyor"}
        ],
        "metal": [
            {"name": "Altın (gr)", "price": round(gold_gram, 2)},
            {"name": "Gümüş (gr)", "price": round(silver_gram, 2)}
        ]
    }

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("data.json başarıyla güncellendi")

if __name__ == "__main__":
    main()
