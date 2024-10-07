import requests
import json
base_url = "https://api.coindesk.com/v1/bpi"


def get_coin_info (name) :
     url = f"{base_url}/currentprice.json"
     response = requests.get(url)

     if response.status_code == 200 :
         Poke_data = response.json()
         return Poke_data
     else:
         print (f"Don't have {response.status_code}")

pokemon = str(input())
poke_info = get_coin_info(pokemon)

if poke_info:
    json_print = json.dumps(poke_info,indent= 5)
    print(json_print)
