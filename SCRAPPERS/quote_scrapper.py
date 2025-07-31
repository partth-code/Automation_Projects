import requests
from bs4 import BeautifulSoup
import csv
import time
import random

'''
Defining URL to READ
Reading the URL
Creating SOUP of HTML
Extracting QUOTES from the page
turning page
and then extracting relevant info
'''

#Defining URL
base_url = 'https://quotes.toscrape.com'
page_url = '/page/1/'
all_info = []

try:
    while (page_url):
        
        print(f"Scrapping Page: {base_url+page_url}")
        res = requests.get(base_url+page_url)
        time.sleep(random.uniform(1,3))    
        res.raise_for_status()
        
        #Creating Soup
        soup  = BeautifulSoup(res.text,'html.parser')
        
        
        #Extractingthe Quotes
        quotes = soup.select('div.quote')
        
        #Extracting Info
        for quote in quotes:
            text = quote.find('span',class_ = 'text').text.strip()
            author_name = quote.find('small',class_ ='author').text.strip()
            tags = [tag.text for tag in quote.find_all('a',class_ = 'tag')]
            all_info.append([text,author_name,",".join(tags)])
        
        
        next_btn = soup.find('li',class_='next')
        page_url = next_btn.find('a')['href'] if next_btn else None
        
    with open('Quote_Info.csv','w',newline='',encoding='utf-8') as file:
        writer  = csv.writer(file)
        writer.writerow(['Quote','Author','Tags'])
        writer.writerows(all_info)
    
    print("Stored All the Above Codes in Csv")
    
except Exception as e:
    print("An error Occoured while Scrapping: ",e)