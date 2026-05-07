import requests
from bs4 import BeautifulSoup

url = "https://www.myhome.ge/ka/s/ბინები-თბილისი?Keyword=&AdTypeID=1&PrTypeID=1"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
print(response.status_code)
print(len(response.text))