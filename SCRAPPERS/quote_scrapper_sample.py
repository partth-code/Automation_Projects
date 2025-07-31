import requests
from bs4 import BeautifulSoup
import random
import time
import csv

'''

Reading the Url
Extracting the quotes
then extracting the asked info

'''

base_url = "http://quotes.toscrape.com"
url = "/page//" #Url we are scrapping
all_data = []


try:

    while url:
        print(f"Scrapping {base_url+url}")
        res = requests.get(base_url+url) #reading the url content
        time.sleep(random.uniform(1,3))
        
        res.raise_for_status()
        
        soup = BeautifulSoup(res.text ,'html.parser')
        
        
        #Extracting All Quotes
        quotes = soup.select('div.quote')
        # print(quotes)
        
        for quote in quotes:
            text = quote.find('span').text.strip()
            author = quote.find('small',class_ = 'author').text.strip()       
            tags = [tag.text for tag in quote.find_all('a',class_ = 'tag') ] 
            all_data.append([text , author , ",".join(tags)])
            
        
        #Next page
        next_btn = soup.find('li',class_ ='next')
        url = next_btn.find('a')['href'] if next_btn else None
        
    with open('Quote_Info.csv','w',newline="",encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Quote','Author','Tags'])
        writer.writerows(all_data)
    
    print("All Ouotes Saved to CSV")

except Exception as e:
    print("An Error Occoured while Scrapping: ",e)        
        


