from urllib.request import Request,urlopen
import urllib.request
from bs4 import BeautifulSoup
import urllib.request

class CountryRestrictions():
    def __init__(self,country,url):
        self.country = country
        self.url = url

    def scrape(self):
        page=urllib.request.Request(self.url,headers={'User-Agent': 'Mozilla / 5.0(Windows NT 6.1) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 41.0 .2228 .0 Safari / 537.3'}) 
        infile=urllib.request.urlopen(page).read()
        data = infile.decode('ISO-8859-1') 
        soup = BeautifulSoup(data,features="html.parser")
        entrycontent = soup.find('div', class_='entry-content')
        detailedheading = entrycontent.find('h2', text = 'Detailed Travel Advisory')
        detailed = detailedheading.find_next_sibling('p')
        self.restrictionsraw = detailed.getText()
        return self
