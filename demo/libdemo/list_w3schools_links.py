import requests
from bs4 import BeautifulSoup

resp = requests.get("https://www.w3schools.com")
bs = BeautifulSoup(resp.text, 'html.parser')

for a in bs.find_all('a'):
    text = a.text.strip()
    link = a['href']   # Take value from attribute href
    if link.startswith("javascript") or link.startswith("http"):
        continue

    if len(text) > 0:
       print(f"{text:50} {link}")
