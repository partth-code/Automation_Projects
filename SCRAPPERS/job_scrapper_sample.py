import requests
from bs4 import BeautifulSoup
import time 
import random


def scrape_remote_job():
    
    
    header = {
        "User-Agent":"Mozilla/5.0"
    }
    
    url = "https://remoteok.com/remote-dev-jobs"
    res= requests.get(url,headers= header)
    
    if res.status_code!= 200:
        print("Failed to retrieve jobs..")
        return 
    
    soup = BeautifulSoup(res.text , 'html.parser')
    
    jobs = soup.find_all('tr' , class_ = "job")
    
    for job in jobs:
        try:
            text = job.find('h2').get_text(strip=True)
            company = job.find('h3').get_text(strip = True)
            location = job.find('div' , class_ = 'location')
            location = location.text.strip() if location else 'Remote'
            tags = [tag.get_text(strip=True) for tag in job.find('span' , class_ = 'tag') ]
            
            
            print(f'Job Title: {text}\nCompany: {company}\nLocation: {location}\nTags: {",".join(tags)}')
            print("-"*40)
            
            
        except Exception as e:
            continue   
        
    
        
if __name__ == "__main__":
    scrape_remote_job()