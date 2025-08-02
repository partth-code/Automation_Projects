from dotenv import load_dotenv
import os
import requests
import schedule
from win10toast import ToastNotifier
import time

load_dotenv()

API_KEY = os.getenv('CRYPTO_API_KEY')
BASE_URL = 'https://api.coingecko.com'

THRESHOLD_BTC = 1000
THRESHOLD_ETH = 2000

def get_crypto_prices():
    
    url = f"{BASE_URL}/api/v3/simple/price"
    
    params = {
        'ids':'bitcoin,ethereum',
        'vs_currencies'  :'usd'
    }
    
    response = requests.get(url,params=params)
    data = response.json()
    
    btc_price = data['bitcoin']['usd']
    eth_price = data['ethereum']['usd']
    
    return btc_price,eth_price


def check_threshold(btc_price,eth_price):
    
    print(f"BTC : {btc_price}\nETH: {eth_price}")
    toast = ToastNotifier()
    
    if btc_price>=THRESHOLD_BTC:
        
        toast.show_toast(title='Bitcoin Price Alert' , msg = 'BitCoin Prices Exceeded the Threshold Price' , duration=5)
    
    if eth_price>=THRESHOLD_ETH:
        toast.show_toast(title='Etherium Price Alert',msg = "Ethereum Price Exceeded the Threshold Price" , duration=5)
    
    
if __name__ == "__main__":
    schedule.every(4).seconds.do(lambda: check_threshold(*get_crypto_prices()))
    
    while True:
        schedule.run_pending()
        time.sleep(2)
        