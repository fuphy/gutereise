#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
from time import time
#import pymysql
#import pymysql.cursors
import sys
import re
from fake_useragent import UserAgent
import json
from datetime import datetime
import pandas as pd

"""
currentSecond= datetime.now().second
currentMinute = datetime.now().minute
currentHour = datetime.now().hour

currentDay = datetime.now().day + 23
currentMonth = datetime.now().month
currentYear = datetime.now().year

print('Day: ', currentDay)
print('Month: ', currentMonth)
"""

start_time = time()

restListLink = "https://www.expedia.co.in/Flights-Search?trip=roundtrip&leg1=from%3AMunich%2C%20Germany%20(MUC)%2Cto%3AChennai%2C%20India%20(MAA)%2Cdeparture%3A21%2F06%2F2018TANYT&leg2=from%3AChennai%2C%20India%20(MAA)%2Cto%3AMunich%2C%20Germany%20(MUC)%2Cdeparture%3A27%2F06%2F2018TANYT&passengers=adults%3A1%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.co.in"
print(restListLink)
ua1 = UserAgent()
randomHeader = {'User-Agent':str(ua1.random)}
page = requests.get(restListLink, randomHeader)
soup = BeautifulSoup(page.content, 'html.parser')
restNameList = len(soup.find_all('script', {'id': 'cachedResultsJson'}))
priceJson = soup.find_all('script', {'id': 'cachedResultsJson'})[0].get_text()
parsed = json.loads(priceJson)
dict_train = parsed['content']
dict_train = json.loads(dict_train)
#dict_train = stringCom.to_dict()

airlineList = list()
priceList = list()

"""
print(stringCom)
for x in range(100):
    try:
        stringCom = stringCom.split(',"formattedRoundedPrice":"', 1)
        stringCom = stringCom[1].split('"', 1)
        price = stringCom[0]
        stringCom = stringCom[1].split('airlineName":"', 1)
        stringCom = stringCom[1].split('"', 1)
        airline = stringCom[0]
        stringCom = stringCom[1]
        if(airline == ''):
            z = 0
        else:
            if airline not in airlineList:
                airlineList.append(airline)
            price = price.split('Rs.', 1)
            price = price[1].split(',', 1)
            price = price[0] + price[1]
            price = int(price)
            priceList.append(price)
            print(airline, ' available at ', price)
    except:
        x = 0

for i in range(len(airlineList)):
    print(airlineList[i])
    print(priceList[i])
"""

train = pd.DataFrame.from_dict(dict_train['legs'], orient='index').reset_index()

finalDf = pd.DataFrame()

finalDf['naturalKey'] = train['naturalKey']
finalDf['price'] = train['price']
finalDf['carrierSummary'] = train['carrierSummary']

x = finalDf['carrierSummary'].to_dict()
y = finalDf['price'].to_dict()

aList = list()
pList = list()

for i in range(len(x)):
    print(x[i]['airlineName'], ' available at ', y[i]['exactPrice'])
    if(x[i]['airlineName'] == ''):
        print('Skip')
    else:
        aList.append(x[i]['airlineName'])
        pList.append(y[i]['exactPrice'])

newDf = pd.DataFrame()

newDf['airline'] = aList
newDf['price'] = pList

newDf = newDf[newDf['price'].isin(newDf.groupby('airline').min()['price'].values)]
newDf = newDf.drop_duplicates(subset = ['airline', 'price'], keep = 'first')

print(newDf)

end_time = time()
time_taken = end_time - start_time

print("Total time taken in seconds: ", time_taken)
