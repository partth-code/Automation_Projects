import requests
from dotenv import load_dotenv
import os

load_dotenv()


#Setting Up Base URL
API_KEY = os.getenv('API_KEY')
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'


#Enterign the City Name
city = input("Enter your City: ")

#Preparing the Request URL
params = {
    'q':city,
    'appid': API_KEY,
    'units': 'matric' #'imperial for fahrenhiet'
}


response = requests.get(BASE_URL,params)


if  response.status_code == 200:
    data = response.json()
    main = data['main']
    weather = data['weather'][0]
    
    
    print(f"City: {main['city']}")
    print(f"Temprature: {main['temp']}C")
    print(f"Humidity: {main['humidity']} %")
    print(f"Weather: {weather['description']}")

else:
    print("An Error Occoured While Retreaving the Weeather Data")