import smtplib
from email.message import EmailMessage
import os
import mimetypes

email = EmailMessage()

email['from'] = 'parthcompiler@gmail.com'
email['to'] = 'sample@gmail.com'
email['subject'] = "A sample Email with Attachment"

email.set_content("A sample emial")

#Setting Attachment

file_path = ""
file_name = os.path.basename(file_path)


#Guessing File PAth and encoding

mime_type,_ = mimetypes.guess_type(file_name)
mime_main,mime_sub = mime_type.split('/')


#Read and Attach
with open(file_path,'rb') as file:
    file_data = file.read()
    email.attach(file_data,maintype = mime_main , subtype = mime_sub , file_name = file_name)


server = 'smtp.gmail.com'
port = 587


sender_email = 'parthcompiler@gmail.com'
sender_password = 'hixf aapy ejcn glqd'

with smtplib.SMTP(server,port) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(sender_email , sender_password)
    smtp.send_message(email)
    