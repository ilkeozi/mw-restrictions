from CountryRestrictions import CountryRestrictions
from WegoCountrylist import WegoCountryList

url = 'https://blog.wego.com/quarantine-guidelines-for-travel-in-all-countries/'

wego = WegoCountryList(url)
countrylist = wego.Parse()
for country in countrylist:
    country.scrape()
    print(country.restrictionsraw)


