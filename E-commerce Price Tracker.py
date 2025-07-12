#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.in/dp/B0BSNPQJ67"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def check_price():
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text().strip()
    price = soup.find('span', {'class': 'a-price-whole'})
    if price:
        price_value = float(price.get_text().replace(',', '').replace('₹', '').strip())
        if price_value < 50000:
            send_email(title, price_value)

def send_email(product, price):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your_email@gmail.com', 'your_password')
    subject = f'Price Drop Alert: {product}'
    body = f'Price dropped to ₹{price}\nCheck the link: {URL}'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('your_email@gmail.com', 'target_email@gmail.com', msg)
    server.quit()

check_price()

