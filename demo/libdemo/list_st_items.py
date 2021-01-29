import requests
from bs4 import BeautifulSoup
from datetime import *

resp = requests.get("http://www.srikanthtechnologies.com/rss.xml")
bs = BeautifulSoup(resp.text, 'lxml-xml')

for item in bs.find_all('item'):
    title = item.title.text.strip()
    link = item.link.text.strip()
    pd_text = item.pubDate.text.strip()[5:16]
    pubdate = datetime.strptime(pd_text, '%d %b %Y')
    days = (datetime.now() - pubdate).days
    print(title)
    print(link)
    print(days, 'days old')
    print('-' * 80)
