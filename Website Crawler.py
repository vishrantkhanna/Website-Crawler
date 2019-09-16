import requests
from bs4 import BeautifulSoup

URL = 'https://vishrantkhanna.com/?s=1'

html = requests.get(URL).text
bs = BeautifulSoup(html, 'html.parser')
for link in bs.find_all('h2', {'class': 'entry-title'}):
    a = link.find('a', href=True)
    href = "https://vishrantkhanna.com/" + a.get('href')
    title = link.string
    print(href)
    print(title)