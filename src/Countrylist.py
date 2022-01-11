from urllib.request import Request,urlopen
import urllib.request
from bs4 import BeautifulSoup, NavigableString, Tag
import requests

import urllib.request

url = 'https://blog.wego.com/quarantine-guidelines-for-travel-in-all-countries/'




page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla / 5.0(Windows NT 6.1) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 41.0 .2228 .0 Safari / 537.3'}) 
infile=urllib.request.urlopen(page).read()

data = infile.decode('ISO-8859-1') 
soup = BeautifulSoup(data)
countrysoups = soup.find_all('h3')
linksoups = soup.find_all('a',string = 'here.') 

for linksoup in linksoups:
    parent = linksoup.parent.previous_element.previous_element.previous_element
    country = parent
    print(country + "|" + linksoup['href']) 




