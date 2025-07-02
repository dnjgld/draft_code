from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText
mail_host = 'smtp.gmail.com'  
mail_user = ''
mail_pass = 'cbbtfmticugsvqlm'   
sender = ''  
receivers = ['']  

message = MIMEMultipart()
message['Subject'] = 'Alert: not running' 
message['From'] = sender 
message['To'] = receivers[0]  

text = MIMEText('...','plain','utf-8')
message.attach(text)

# image_open=open('C:\\DengJinglong.jpg','rb')
# image=MIMEImage(image_open.read())
# image.add_header('Content-ID','')
# message.attach(image)


try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host,587)
    smtpObj.starttls()
    smtpObj.login(mail_user,mail_pass) 
    smtpObj.sendmail(
        sender,receivers,message.as_string()) 
    smtpObj.quit() 
    print('success')
except smtplib.SMTPException as e:
    print('error',e) 