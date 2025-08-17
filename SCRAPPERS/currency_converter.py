import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def convert_currency(amount,from_currency,to_currency):
    api_key = os.getenv("EXCHANGERATE_API_KEY")
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    
    
    if True:
            res = requests.get(url)  #response
        

            data = res.json()
            
            if data.get('result') == 'success':
                rate = data['conversion_rates'].get(to_currency)
                
                converted_amt = amount*rate
                date_str = data['time_last_update_utc']
                
                dt = datetime.strptime(date_str , "%a, %d %b %Y %H:%M:%S %z")
                
                only_date = dt.strftime("%Y-%b-%d")
                
                return {
                    "currency from": from_currency,
                    "currency to" : to_currency,
                    "inital amout": f"{amount}  {from_currency}",
                    "converted amount": f"{converted_amt}  {to_currency}",
                    "date": only_date
                }

if __name__ == "__main__":
     amount = float(input("Enter Amount: "))
     
     from_currency = input("From Currency (e.g., USD): ").upper()
     to_currency = input("To Currency (e.g. ,INR): ").upper()
     
     result = convert_currency(amount,from_currency,to_currency)
     print(result)