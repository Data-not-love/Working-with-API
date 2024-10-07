import time

import requests
import json

base_url = "https://api.coingecko.com/api/v3"



def get_coin_info (Coin):
    url = f"{base_url}/coins/{Coin}"
    response = requests.get(url)
    if response.status_code == 200:
        coin_data = response.json()
        return coin_data
    else:
        print(f"Failed to retrieve data for {Coin}. Status code: {response.status_code}")
        return None


coin = input("Name : ?")

    # Bạn có thể thay bằng coin khác như "ethereum", "litecoin", v.v.
coin_info = get_coin_info(coin)
if coin_info:
    pretty_print = json.dumps(coin_info['market_data']['current_price'], indent=4)
    print("Real-time price data:", pretty_print)
