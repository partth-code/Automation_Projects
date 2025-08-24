from dotenv import load_dotenv
import os
import smtplib
from email.message import EmailMessage
from email.utils import make_msgid
import requests
import random
import time
load_dotenv()

def quote():
    url = 'https://zenquotes.io/api/quotes/'
    
    res = requests.get(url) #response
    time.sleep(random.uniform(1,3))
    
    data = res.json()
    
    #Fetching Random Quote
    quote_info = random.choice(data)
    
    
    return f"{quote_info['q']}\nby {quote_info['a']}"
    
    

#Setting Up Server and Port
server = 'smtp.gmail.com'
port = 587


sender_email = 'parthcompiler@gmail.com'
sender_password = os.getenv("EMAIL_PASSWORD")
reciever_email = 'aquasunroyals@gmail.com'


email = EmailMessage()

email['from'] = sender_email
email['to'] = reciever_email
email['subject'] = "Motivational Email"

email.set_content(quote())

with smtplib.SMTP(server,port) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(sender_email,sender_password)
    smtp.send_message(email)