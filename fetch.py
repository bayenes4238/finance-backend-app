import requests
import json

# CoinGecko API fonksiyonu
def get_coin(id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={id}&vs_currencies=usd"
    r = requests.get(url)
    return r.json()[id]['usd']

# USD/TRY
def get_usdtry():
    r = requests.get("https://api.exchangerate.host/latest?base=USD&symbols=TRY")
    return r.json()["rates"]["TRY"]

def main():
    usdtry = get_usdtry()

    btc = get_coin("bitcoin")
    eth = get_coin("ethereum")

    # Altın / Gümüş ons USD → gram TL
    gold_ons = get_coin("gold")
    silver_ons = get_coin("silver")
    gold_gram = (gold_ons * usdtry) / 31.1035
    silver_gram = (silver_ons * usdtry) / 31.1035

    data = {
        "coin": [
            {"name": "BTC", "price": round(btc,2)},
            {"name": "ETH", "price": round(eth,2)},
            {"name": "USDT", "price": "Üzerinde çalışılıyor"},
            {"name": "XRP", "price": "Üzerinde çalışılıyor"}
        ],
        "bist": [
            {"name":"THYAO","price":"Üzerinde çalışılıyor"},

