import requests
from bs4 import BeautifulSoup
import random
import time
from datetime import datetime

def news_scrapper():
    headlines = []
    
    top_headlines = []
    url = "https://www.bbc.com/"
    
    res = requests.get(url)
    time.sleep(random.uniform(1,3))
    
    soup = BeautifulSoup(res.text , 'html.parser')
    
    tags = soup.find_all('h2')
    
    for tag in tags:
        text = tag.getText(strip= True)
        headlines.append(text)
        if len(headlines) == 5:
            break

    with open('Headlines.txt' , 'w'  , encoding='utf-8') as file:
        
        file.writelines(f"Date: [{datetime.today().strftime('%d-%m-%Y')}]\n")
        for headline in headlines:
            file.writelines(f"{headline}\n")
        
        file.writelines('\n')

if __name__ == "__main__":
    news_scrapper()