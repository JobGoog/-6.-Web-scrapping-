import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
# import json


def get_headers():
    return Headers(browser="firefox", os="win").generate()


DATA_URL = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'
# KEYWORDS = ['Django', 'django', 'Flask', 'flask']


response = requests.get(DATA_URL, )
response_text = response.text
print(response_text)