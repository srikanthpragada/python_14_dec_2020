import requests
from bs4 import BeautifulSoup

resp = requests.get("http://www.srikanthtechnologies.com")
bs = BeautifulSoup(resp.text, 'html.parser')

for a in bs.find_all('a'):
    text = a.text.strip()
    link = a['href']  # Take value from attribute href
    if link.startswith("javascript") or link == '#':
        continue

    if len(text) > 0:
        print(text)
        if not link.startswith('http'):
            link = 'http://www.srikanthtechnologies.com/' + link

        print(link)
        print('-' * 50)
