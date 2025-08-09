import threading
from tkinter import Tk , Label 
from tkinter import messagebox
import os
from dotenv import load_dotenv
import requests
from plyer import notification
import schedule
import time


'''
Creating an GUI
it dsplays current dollar value of bitcoin and ethereum
if the value exceeds the threshold we get a notification
'''

load_dotenv()

class CryptoTracker:
    def __init__(self,root):
        self.root = root
        self.root.title("Crypto Price Tracker")
        self.root.geometry("400x200")


        #Setting Threshold
        self.BTC_THRESHOLD = 3000
        self.ETH_THRESHOLD = 4000
        
        #Setting up placeholder value for bitcion and ethereum
        self.btc_val,self.eth_val = self.predict_val()

        
        #Settingup the Window
        self.setup()
    
    def setup(self):
        
        
        #Label and Price For Bitcoin
        Label(self.root , text = f"Bitcoin Value in Dollars: " , font = ('Arial',12,'bold')).grid(row=0,column=0)
        
        self.btc_label = Label(self.root , text = f"{self.btc_val}$",  font = ('Arial',12,'normal') , fg = 'green')
        self.btc_label.grid(row=0,column=1 , pady = 50)
        
        
        #Label and Price for Ethereum
        Label(self.root , text =f"Ethereum Value in Dollars: " ,  font = ('Arial',12,'bold')).grid(row=1,column=0)
        
        self.eth_label  =Label(self.root , text = f"{self.eth_val}$" , font = ('Arial',12,'normal') , fg = "green")
        self.eth_label.grid(row=1 , column=1 , pady= 10)
        
        
        #schudling Notification
        schedule.every().hour.do(self.crypto_notifier)
        
        self.schedular_thread = threading.Thread(target=self.schedular , daemon=True)
        self.schedular_thread.start()
    
    def schedular(self):
        
        while True:
            schedule.run_pending()
            time.sleep(2)
            
    def predict_val(self):
        
        BASE_URL = 'https://api.coingecko.com'
        API_KEY = os.getenv("CRYPTO_API_KEY")
        
        
        url = f"{BASE_URL}/api/v3/simple/price"
        
        
        params = {
            'ids':'bitcoin,ethereum',
            'vs_currencies': 'usd'
        }
        
        if True:
            response = requests.get(url , params=params)
            data = response.json()
            
            if 'bitcoin' in data and 'usd' in data['bitcoin']:
                self.btc_val = data['bitcoin']['usd']
                
            else:
                raise ValueError(f"Bitcoin Price not Found in API Response")
            
            if 'ethereum' in data and 'usd' in data['ethereum']:
                self.eth_val = data['ethereum']['usd']
            
            else:
                raise ValueError(f"Ethereum Price not Found in API Response")
            
            
            return self.btc_val,self.eth_val
        
        
        
        else:# Exception as e:
            messagebox.showerror(title = "Error Message" , message= str(e))
            return self.btc_val ,self.eth_val
        
        
    def notify(self,**kwargs):
            
        title = kwargs.pop('title',"Title")
        message = kwargs.pop('message','This is a sample message')
        span = kwargs.pop('span',5)
            
        notification.notify(
            title = title,
            message = message,
            timeout = span
            )
    
    def crypto_notifier(self):
        
        self.btc_val,self.eth_val = self.predict_val()
        
        self.btc_label.config(text = f"{self.btc_val}$")
        self.eth_label.config(text = f"{self.eth_val}$")

                
        if(self.eth_val>self.ETH_THRESHOLD):
            self.notify(title = "Ethereum Price Alert" , message = "Ethereum Price Exceeded The Specified Threshold" , span = 5)
        
        if(self.btc_val>self.BTC_THRESHOLD):
            self.notify(title = "Bitcoin Price Alert" , message = "Bitcoin Price Exceeded The Specified Threshold" , span = 5)
        
        




if __name__ == "__main__":
    
    root = Tk()
    app = CryptoTracker(root)
    root.mainloop()