from tkinter import Tk , Frame , Label , Entry , StringVar , Button
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

class CurrencyCoverter:
    def __init__(self,root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry('400x300')
        
        self.setup()
        
    def setup(self):
        
        self.title()
        self.converter_gui()
        
        
    def title(self):
        self.titleFrame = Frame(self.root , height=100 , bg = 'grey' )
        self.titleFrame.pack(fill='x')
        
        Label(self.titleFrame , text = "Currency Converter" , font = ( 'Arial',20 , 'bold') ,bg = 'grey' , fg = 'white').pack(pady = 20)
        

    def converter_gui(self):
        self.mainFrame = Frame(self.root , height= 600 ,bg = 'lightgrey' )
        self.mainFrame.pack(fill='x')
        
        Label(self.mainFrame , text = "From Currency: ").grid(row=0,column=0 , pady=20 , padx=30)
        
        self.fromCurrency = StringVar()
        Entry(self.mainFrame , width=30 , textvariable=self.fromCurrency).grid(row=0 ,column=1)
        
        
        Label(self.mainFrame , text = "To Currency: ").grid(row=1 , column=0 )
        
        self.toCurrency = StringVar()
        Entry(self.mainFrame , width=30 , textvariable=self.toCurrency).grid(row=1,column=1)
        
        Label(self.mainFrame , text = "Amount: " ).grid(row=3 , column=0)
        
        self.amount = StringVar()
        Entry(self.mainFrame , width= 30 , textvariable= self.amount).grid(row=3 , column=1 , pady =20,padx= 30 )
        
        Button(self.mainFrame , text = "Convert", font = ('Airal',10 , 'bold') , fg = 'white' , bg = 'black' , command = self.convert).grid(row = 4 , column=0 ,padx =30, sticky='nsew')
    
        self.coversionResult = Label(self.mainFrame ,bg = "lightgrey")
        self.coversionResult.grid(row=4 , column=1)


    def do_conversion(self , amount=1 , currency_from='USD' , currency_to = 'INR'):
        
        api_key = os.getenv("EXCHANGERATE_API_KEY")
        
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{currency_from}"
        
        try:
            response = requests.get(url)
            data = response.json()
            
            if data.get('result') == 'success':
                rate = data['conversion_rates'].get(currency_to)
                
                converted_amount = amount*rate
                
                date_str = data["time_last_update_utc"]
                
                dt = datetime.strptime(date_str ,"%a, %d %b %Y %H:%M:%S %z")
                
                date = dt.strftime("%d-%b-%Y")
                self.coversionResult.config(text =  f"Converting from {currency_from} to {currency_to}\nDate: {date}\n {amount}{currency_from} = {converted_amount}{currency_to}" , fg = "green")
            
            else:
                self.coversionResult.config(text =  "An Erorr Occoured while collecing the Data" , fg = 'red')
        
        except Exception as e:
            
            
            self.coversionResult.config(text =  "An Erorr Occoured while collecing the Data" , fg = 'red') 
            print(e)
                
    def convert(self):
        convertFrom = self.fromCurrency.get().strip().upper()
        convertTo = self.toCurrency.get().strip().upper()
        try:
            amount = float(self.amount.get().strip())
            
            if amount<=0:
                raise ValueError("Enter a valied amount")
            
            self.do_conversion(amount , convertFrom ,convertTo)

            
        except:
            self.coversionResult.config(text =  "Enter a valied amount" , fg = 'red')
        
        
        
        
if __name__ == "__main__":
    root =Tk()
    app = CurrencyCoverter(root)
    root.mainloop()
    
    
