from urllib.request import Request,urlopen
import urllib.request
from bs4 import BeautifulSoup, NavigableString, Tag
import requests
import urllib.request
from CountryRestrictions import CountryRestrictions


class WegoCountryList:

  def __init__(self,url):
    self.url = url

  def Parse(self):
    page=urllib.request.Request(self.url,headers={'User-Agent': 'Mozilla / 5.0(Windows NT 6.1) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 41.0 .2228 .0 Safari / 537.3'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('ISO-8859-1') 
    soup = BeautifulSoup(data,features="html.parser")
    countrysoups = soup.find_all('h3')
    linksoups = soup.find_all('a',string = 'here.') 
    list = []
    for linksoup in linksoups:
      parent = linksoup.parent.previous_element.previous_element.previous_element
      country = parent
      list.append( CountryRestrictions(country,linksoup['href']))
    return list