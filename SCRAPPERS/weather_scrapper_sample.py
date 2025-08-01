import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units':'metric'
    }
    
    try:
        response = requests.get(BASE_URL,params)
        data = response.json()
            
            
        if data['cod'] == 200:
            main = data['main']
            weather = data['weather'][0]
            
            
            print(f"City: {city}")
            print(f"Temprature: {main['temp']}C")
            print(f"Humidity: {main['humidity']}%")
            print(f"Pressure: {main['pressure']} hPa")
            print(f"Weather Discription: {weather['description'].capitalize()}")
            
            
        else:
            print("City not Found!")
    
    except Exception as e:
        print("Error Occoured: ",e)
        
        
if __name__ == "__main__":
    city_name = input("Enter your City: ")
    get_weather(city_name)