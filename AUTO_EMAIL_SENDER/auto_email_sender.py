import smtplib
from email.message import EmailMessage

#Creating Email

email = EmailMessage()
email['from'] = "parthcompiler@gmail.com"
email['to'] = 'aquasunroyals@gamil.com'
email['subject'] = "This is a sample Email"

email.set_content("This is a sample email.Hope you like it")

#Gmail SMTP Server

smtp_server = 'smtp.gmail.com'
port = 587 

#Login And Send
sender_email = 'parthcompiler@gmail.com'
sender_password = 'hixf aapy ejcn glqd'


with smtplib.SMTP(smtp_server,port) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(sender_email,sender_password)
    smtp.send_message(email)