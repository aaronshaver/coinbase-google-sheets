import time
import requests

def get_eth_usd_sell_price():
    url = 'https://api.coinbase.com/v2/prices/ETH-USD/sell'
    response = requests.get(url)
    return response.text

while True:
    price = get_eth_usd_sell_price()
    print(price)
    # do update
    time.sleep(60)
