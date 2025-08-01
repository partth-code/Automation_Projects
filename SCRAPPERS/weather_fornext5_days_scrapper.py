import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL_WEATHER = 'http://api.openweathermap.org/data/2.5/weather'
BASE_URL_FORCAST = 'https://api.openweathermap.org/data/2.5/forecast'


def predict_weather(city):
    
    params = {
        'q':city,
        'appid':API_KEY,
        'units':'metric'
    }
    
    
    res = requests.get(BASE_URL_WEATHER,params)
    data = res.json()

    try:
        
        if(data['cod'] == 200):
            main = data['main']
            weather = data['weather']
            
            
            
            print(f"City: {city}")
            print(f"Temprature: {main['temp']}C")
            print(f"Humidity: {main['humidity']}%")
            print(f"Weather Discription: {weather['description']}")
        
        else:
            print("City not Found")
    
    except Exception as e:
        print("An Error Occoured while getting the weather data: ",e)
        


def predict_forcast(city):
    
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    

        
    res = requests.get(BASE_URL_FORCAST,params)
    data = res.json()

    try:
            
            if data['cod'] == "200":
                
                print(f'\n% Day forcast for City {city.title()}: ')
                
                for forcast in data['list']:
                    dt = datetime.fromtimestamp(forcast['dt'])
                    temp = forcast['main']['temp']
                    desc = forcast['weather'][0]['description']
                    
                    if dt.hour == 11:
                        print(f"{(dt.strftime('%Y-%m-%d %H:%M'))} - {temp} C - {desc.capitalize()}")
            
            else:
                print("City Not Found")
                
    except Exception as e:
            print("Error Occoured: ",e)
            

if __name__ == "__main__":
    city_name = input("Enter city Name: ")
    predict_forcast(city_name)
    print('\n')
    predict_weather(city_name)          
        