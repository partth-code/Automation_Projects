import requests
from dotenv import load_dotenv
import csv
import os

API_KEY = os.getenv('API_KEY')
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

cities = input("Enter Cities(seperate them by ,): ").split(',')

params = {
    'appid': API_KEY,
    'units': 'matric'
}

for city in cities:
    params['q'] = city
    
    reponse = requests.get(BASE_URL,params)
    
    data = reponse.json()
    main = data['main']
    weather = data['weather']
    
    weather_of_city = [main['city'],main['temp'],weather['discription']]
    

csv_path = 'd:\\creatios\\SCRAPPING_WEATHEr_INFO\\weather_info.csv'
text_path = 'd:\\creatios\\SCRAPPING_WEATHEr_INFO\\weather_info.txt'

if not(os.path.exists(csv_path)):
    with open(csv_path,'w') as file:
        writer  = csv.writer()
        writer.writerow(['City','Temprature','Weather_Discription'])
        writer.writerow(weather_of_city)
else:
    with open(csv_path,'a') as file:
        writer = csv.writer()
        writer.writerow(weather_of_city)

if not(os.path.exists(text_path)):
    with open(text_path,'w') as file:
        file.writelines(weather_of_city.join(' '))
else:
    with open(text_path, 'a') as file:
        file.writelines(weather_of_city.join(' '))