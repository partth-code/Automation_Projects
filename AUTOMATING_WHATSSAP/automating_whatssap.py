'''
1- twidio client setup
2- user input
3 - sceheduling logic
4 - send message
'''

#Essential Imports
from twilio.rest import Client
from datetime import datetime ,timedelta
import time
import os



#Twidio Credintials

account_sid = 'AC16b80548975e492bac327bae9fd23fa7'#os.getenv('ACC_SID')
auth_token = '2897aa4633e495e32a220764d9cd1786'#os.getenv('AUTH_TOKEN')

#Creating Client to Send Messages
client = Client(account_sid,auth_token)

#Creating Function to Send whatssap Message

def send_whatsaap_message(reciever_phno , message_body):
    try:
        message =  client.messages.create(
            from_= 'whatsapp:+14155238886',
            body = message_body,
            to =  f'whatsapp:{reciever_phno}')
        
        print(f"Message Sent Successfully!! Message sID: {message.sid}")
    except Exception as e:
        print("An Error Occoured while sending message: ",e)
        
    
#Taking The User Input
name  = input("Enter recipient name: ")
rspnt_no = input("Enter recipinet number with countary code eg +12345: ")
msg_bdy = input(f"Enter the message you want to send to {name}: ")


#Calculating delay in ssending the message
date_str = input("Enter date to send the message (YYYY-MM-DD): ")
time_str = input("Enter time to send the message (HH:MM in 24hr format): ")

#Scheduled Time
scheduled_time = datetime.strptime(f"{date_str} {time_str}" , "%Y-%m-%d %H:%M")
current_time = datetime.now()

#Delayed Time
time_diff = scheduled_time-current_time
delay_sec = time_diff.total_seconds()

if delay_sec <=0 :
    print("The specified time is from past.Please enter future date and time")
else:
    print(f"Message scheduled for recipient {name} and scheduled at {scheduled_time}")
    
    # time.sleep(delay_sec)
    
    send_whatsaap_message(rspnt_no , msg_bdy)
