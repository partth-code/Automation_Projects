import requests
from dotenv import load_dotenv
import os
import csv

load_dotenv()

'''
Scrapping with api

getting the data

storing the data


'''
class WeatherApp:
    def  __init__(self):
        
        self.BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
        self.API_KEY = os.getenv("WEATHER_API_KEY")
        
        with open("Weather_Data.csv", 'w', newline="", encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(("City" , "Temprature(F)" , "Feels Like(F)" , "Humidity(%)" , "Weather Description"))
        
    #Getting Weather Data
    def get_weather_data(self , city):
        
        self.city = city
        
        params = {
            'q':self.city.lower(),
            'appid':self.API_KEY,
            'units':'imperial'
        }
        
        res = requests.get(self.BASE_URL , params) #response
        
        res.raise_for_status()
        
        if res.status_code != 200:
            print("An Error Occuoured , While Parsingt the Weather Data")
            return
        
        data = res.json()
        
        main = data['main']
        weather = data['weather'][0]
        
        self.temp = main['temp']
        self.feels_like = main['feels_like']
        self.humidity = main['humidity']
        self.weather_description = weather['description']
        
        return f"City: {self.city}\nTemprature: {self.temp} || Feel Like: {self.feels_like}\nHumidity: {self.humidity}\nWeather Description: {self.weather_description}"
    
        
    def store_weather_data(self):
        with open("Weather_Data.csv", 'a', newline="", encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow((self.city ,self.temp , self.feels_like , self.humidity , self.weather_description))
            
        
        
        
if __name__ == "__main__":
    
    app  = WeatherApp()
    
    while True:
        location =input("Enter the location for which you want the weather: ").strip().lower()
        if location=='exit':
            break
        print(app.get_weather_data(location))
        app.store_weather_data()