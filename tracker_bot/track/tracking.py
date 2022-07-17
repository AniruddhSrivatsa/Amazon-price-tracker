import requests
from bs4 import BeautifulSoup


def checker(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language' : 'en-US,en;q=0.5',
    'Accept-Encoding' : 'gzip',
    'DNT' : '1', # Do Not Track Request Header
    'Connection' : 'close'
    }
    r=requests.get(url, headers=headers)
    soup=BeautifulSoup(r.text,"lxml")
    name=soup.select_one(selector="#productTitle")
    name=name.getText().strip()

    price=soup.select_one(selector=".a-price-whole")
    print(price)
    price=price.getText().strip()
    print(price.replace(",","").replace(".",""))
    price=float(price.replace(",","").replace(".",""))
    print(price)
    return name,price


