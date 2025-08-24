import smtplib
from email.message import EmailMessage
from email.utils import make_msgid
import mimetypes
from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()

orignal_img = 'sample.jpg'
compressed_img = 'compressed.jpg'

#Resizing the image
img = Image.open('d:\\creatios\\auto_email_sender\\sample.jpg')
img = img.resize((img.height//5,img.width//5))
img.save(compressed_img,quality = 70)

#defining server and port

server = 'smtp.gmail.com'
port = 587

email_sender = 'parthcompiler@gmail.com'
email_password = os.getenv('EMAIL_PASSWORD')
email_reciever = 'parthcompiler@gmail.com'

#Create Email
email  = EmailMessage()

email['from'] = email_sender
email['to'] = email_reciever
email['subject'] = "This is a sample email"


#Making COntent ID CID for Image

img_cid = make_msgid(domain='sample.jpg')
img_cid_clean = img_cid[1:-1]  #Removing <>


#HTML COntent

content_html = f"""
<html>
  <body>
    <h2>Hello!</h2>
    <p>This is an <b>HTML email</b> with an inline image.</p>
    <img src="cid:{img_cid_clean}" alt="My Image"  height = "100"/>
  </body>
</html>
"""

email.set_content("This is fallback content after image")
email.add_alternative(content_html,subtype = 'html')

with open('d:\\creatios\\auto_email_sender\\sample.jpg','rb') as img:
  img_data  = img.read()
  main_type,sub_type = mimetypes.guess_type('sample.jpg')[0].split('/')
  email.get_payload()[1].add_related(img_data,maintype = main_type , subtype = sub_type , cid  = img_cid)

#Send the Email
with smtplib.SMTP(server,port) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login(email_sender,email_password)
  smtp.send_message(email)