from dotenv import load_dotenv
import os
from tkinter import Tk , Label , Button , Entry , StringVar
import requests
from datetime import datetime

'''

App takes User Input for City
Then there will be a button to get weather
Another to get forcast

'''

load_dotenv()

class WeatherApp:
    
    WEATHER_BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
    FORCAST_BASE_URL = 'https://api.openweathermap.org/data/2.5/forecast'
    API_KEY = os.getenv('WEATHER_API_KEY')
    
    def __init__(self,root):
        #Creatilng Window
        self.root = root
        self.root.title('Weather Forcast App')
        self.root.geometry('800x600')
        
        
        #String Variable To Store Coty
        self.city = StringVar()

        self.setup()
        
        
    
    def setup(self):
        
        Label(self.root  , text="Enter Your City: " , font=('Arial',20)).pack(pady=10)
        
        
        self.text_box = Entry(self.root , font=('Arial',10), width= 70 , textvariable= self.city)
        self.text_box.pack(pady= 20)
        
        self.display_info = Label(self.root)
        self.display_info.pack(pady=10)
        
        self.disp_weather  = Button(self.root , text= 'Display Weather' , command= self.show_weather)
        self.disp_weather.pack(pady = 10)
        
        self.disp_forecast= Button(self.root , text = "Display Forecast" , command= self.show_forecast)
        self.disp_forecast.pack(pady = 10)
        
        
    def show_weather(self):
            
            params = {
                'q':self.city.get(),
                'appid':self.API_KEY,
                'units':'metric'  
            }
            
            res = requests.get(self.WEATHER_BASE_URL , params=params)
            
            data = res.json()
            
            if(data['cod'] != 200):
                self.display_info.config(text="Cannot Find The City Data" , fg='red')
                return
            
            main = data['main']
            weather = data['weather'][0]
            
            self.display_info.config(text = f"City: {self.city.get()}\nTemprature: {main['temp'] : .2f}C\nWeather Description: {weather['description']}" , fg = 'green')
            
                
        
    def show_forecast(self):
            params = {
                'q':self.city.get(),
                'appid':self.API_KEY,
                'units':'metric'
            }
            
            res = requests.get(self.FORCAST_BASE_URL , params=params)
            data = res.json()
            
            if(data['cod'] != '200'):
                self.display_info.config(text = "Cannot Find City Data" , fg = 'red')
                return
            
            forecast_info  = []
            for forecast in data['list']:
                dt = datetime.fromtimestamp(forecast['dt'])
                temp = forecast['main']['temp']
                desc = forecast['weather'][0]['description']
                if(dt.hour == 12):
                    forecast_info.append(f"Date Time: {dt.strftime('%Y-%m-%d %H:%M')}\nTemprature: {temp}C\nWeather Description: {desc}")
            
            all_forcast = ('\n'+('-'*20)+'\n').join(forecast_info)    
            self.display_info.config(text=all_forcast, fg='green')
                
            
            


if __name__ == "__main__":
    root  = Tk()
    app = WeatherApp(root)
    root.mainloop()