import requests
from bs4 import BeautifulSoup

import smtplib

    
url = "https://github.com/"
section = "#section-id"

email_address = "milleni00s@gmail.com"
email_password = "robozao242424"



r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
section_content = soup.select_one(section).get_text().strip()

smtp_server = "smtp.example.com"
smtp_port = 587

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(email_address, email_password)

    subject = "Mudanças no site detectadas"
    body = f"A seção {section} do site {url} foi atualizada:\n\n{section_content}"

    message = f"Subject: {subject}\n\n{body}"
    
with open("previous_section.txt","r") as f:
    previous_section_content = f.read().strip()

if section_content != previous_section_content:
    print("Uma mudança foi detectada")
    server.sendmail(email_address, email_address, message)
else:
    print("Nenhuma mudança foi detectada.")