#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

URL = "https://www.bbc.com/news"
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

headlines = [tag.get_text() for tag in soup.find_all('h3')[:10]]  # Sample 10 headlines
for headline in headlines:
    sentiment = TextBlob(headline).sentiment.polarity
    print(f"{headline} | Sentiment: {sentiment}")

