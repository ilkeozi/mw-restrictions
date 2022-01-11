from urllib.request import Request,urlopen
import urllib.request
from bs4 import BeautifulSoup, NavigableString, Tag
import requests

import urllib.request

url = 'https://blog.wego.com/iraq-travel-restrictions-and-quarantine-requirements/'
url = 'https://blog.wego.com/united-kingdom-travel-restrictions-and-quarantine-requirements/'


page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla / 5.0(Windows NT 6.1) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 41.0 .2228 .0 Safari / 537.3'}) 
infile=urllib.request.urlopen(page).read()

data = infile.decode('ISO-8859-1') 
soup = BeautifulSoup(data)
entrycontent = soup.find('div', class_='entry-content')
detailedheading = entrycontent.find('h2', text = 'Detailed Travel Advisory')
detailed = detailedheading.find_next_sibling('p')
print(detailed.getText())