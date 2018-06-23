from selenium import webdriver
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
from datetime import datetime, timedelta
from time import time

"""
def airline_extractor(sampleStr):
    x = sampleStr.split('overflow">', 1)
    x = x[1].split('</span', 1)
    airlineName = x[0]
    return airlineName

def price_extractor(otherStr):
    y = otherStr.split('Rs.</i>', 1)
    y = y[1].split(' </span', 1)
    priceVal = y[0].replace(',', '')
    priceVal = round(float(priceVal) / 75, 2)
    return priceVal
"""
kurl = 'https://www.kayak.com/flights/MUC-PVG/2018-07-20/2018-08-08'
#ct_url = 'https://www.cleartrip.com/flights/international/results?from=MUC&to=MAA&depart_date=11/07/2018&return_date=15/08/2018&adults=1&childs=0&infants=0&class=Economy&airline=&carrier=&intl=y&sd=1529765085608&page=loaded'
#url = 'https://flight.yatra.com/air-search-ui/int2/trigger?type=R&viewName=normal&flexi=0&noOfSegments=2&origin=MUC&originCountry=DE&destination=PVG&destinationCountry=CN&flight_depart_date=20/07/2018&arrivalDate=08/08/2018&ADT=1&CHD=0&INF=0&class=Economy&source=fresco-home&version=1.1'
profile = webdriver.FirefoxProfile()
ua1 = UserAgent()
profile.set_preference('general.useragent.override', str(ua1.random))
driver = webdriver.Firefox(profile)
driver.get(kurl)
html = driver.execute_script('return document.body.innerHTML')
driver.close() 

b_html = bs(html,'html.parser') 
x = b_html.find_all(attrs={"data-name" : "airlines-section"})


"""
air = b_html.find_all('span', class_='clip-overflow')
rs = b_html.find_all('span', class_='filter-price')

aList = []
pList = []

for i in range(len(air)):
    a = airline_extractor(str(air[i]))
    aList.append(a)
    p = price_extractor(str(rs[i]))
    pList.append(p)
"""