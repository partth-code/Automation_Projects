import requests
from dotenv import load_dotenv
import os
import csv


load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

#entering the city
city = input("Enter the city name: ")

#Creating Pameter to give a request
params = {
    'q':city,
    'appid':API_KEY,
    'units':'imperial'
}

response = requests.get(BASE_URL,params)


if(response.status_code == 200):
    data = response.json()
    main = data['main']
    weather = data['weather'][0]
    
    city_weather_info  = [main['city'],main['temp'],weather['discription']]
    
csv_path = 'd:\\creatios\\SCRAPPING_WEATHEr_INFO\\weather_info.csv'
text_path = 'd:\\creatios\\SCRAPPING_WEATHEr_INFO\\weather_info.txt'

if (not os.path.exists(text_path)):
    with open('weather_info.txt','w') as file:
        file.writelines(city_weather_info.join(' '))

else:
    with open('weather_info.txt','a') as file:
        file.writelines(city_weather_info.join(' '))


if (not os.path.exists(csv_path)):
    with open('weather_info.csv','w') as file:
        writer  = csv.writer(file)
        writer.writerow[['City','Temprature','Weather_Info']]
        writer.writerow[city_weather_info]

else:
    with open('weater_info.csv','a') as file:
        writer = csv.writer(file)
        writer.writerow[city_weather_info]