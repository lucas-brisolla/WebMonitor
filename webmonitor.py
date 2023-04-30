import requests 
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = 'smtp.gmail.com'
smtp_port = 587

username = 'robozao@gmail.com'
password = 'robozao424267'

msg = MIMEMultipart()


r = requests.get('https://github.com/lucas-brisolla')

if r.content == r.content:
    print("mudou")
    msg['From'] = username
    msg['To'] = 'lucasabrisolla@gmail.com'
    msg['Subject'] = 'Status do site'
    body = 'Houve uma alteração no site'
    msg.attach(MIMEText(body,'plain'))
    with SMTP(smtp_server, smtp_port) as server:
      server.starttls()
      server.login(username, password)
      server.sendmail(username, 'lucasabrisolla@gmail.com', msg.as_string())
else:
    print("continua igual")