import requests
from bs4 import BeautifulSoup
import time
import random
import csv
import json

def scrape_n_store_jobs():
    
    headers = {
        'User-Agent':'Mozilla/5.0'
    }
    
    url = 'https://remoteok.com/remote-dev-jobs'
    
    res = requests.get(url,headers=headers)
    time.sleep(random.uniform(1,3))
    
    if res.status_code != 200:
        print("Cannot Scrape the server")
        return
    
    
    soup = BeautifulSoup(res.text , 'html.parser')
    
    jobs  = soup.find_all('tr',class_ = 'job')
    print(jobs)
    job_info = []
    
    for job in jobs:
        try:
            text = job.find('h2').get_text(strip=True)
            company = job.find('h3').get_text(strip=True)
            location = job.find('div' , class_ = 'location')
            location = location.get_text(strip= True) if location else "Remote"
            
            tags = [tag.get_text(strip = True) for tag in job.find_all('span',class_ = 'tag')]
            
            print(f"Job: {text}\nCompany: {company}\nLocation: {location}\nTags: {','.join(tags)}\n{"-"*20}")
            job_info.append((text,company,location,','.join(tags)))

        except Exception as e:
            continue
    
    
    with open('Job_Info.csv','w',newline="",encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(['Job','Company','Location','Tags'])
        writer.writerows(job_info)
        
    with open('Job_Info.json' , 'w' , encoding='utf-8')  as file:
        json.dump(job_info , file , indent=4)
        

if __name__ == "__main__":
    scrape_n_store_jobs()