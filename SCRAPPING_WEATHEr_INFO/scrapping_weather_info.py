from dotenv import load_dotenv
import os
import requests

load_dotenv()




class WeatherApp:
    
    def __init__(self):
        self.BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
        self.API_KEY = os.getenv("WEATHER_API_KEY")
        
        
    def get_weather(self,city):
        
        try:
            self.params = {
                'q':city.lower(),
                'appid': self.API_KEY,
                'units':'metric'
            }
            
            res = requests.get(self.BASE_URL , self.params)
            res.raise_for_status()
            
            if (res.status_code != 200):
                return
            
            data = res.json()
            main = data['main']
            weather = data['weather'][0]
            
            wthr_city = city.capitalize()
            temprature = main['temp']
            feels_like = main['feels_like']
            humidity = main['humidity']
            wthr_description = weather['description']
            
            return (f"City: {wthr_city}\nTemprature:{temprature} C || Feels Like: {feels_like} C\nHumidity: {humidity}%\nWeather Description: {wthr_description.upper()}")
            
        
        except Exception as e:
            print(f"Error {e} occoured while fetching the data")
            return
        
        
if __name__ == "__main__":
    app = WeatherApp()
    
    city = input("Enter the city for which you want to know the weather: ").strip().lower()
    print(app.get_weather(city))