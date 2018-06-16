from time import time, sleep
import requests
from datetime import datetime, timedelta
import datetime
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json
import pandas as pd

start_time = time()

def date_splitter(dateToSplit):
    dateToSplit = dateToSplit.split('-', 1)
    year = dateToSplit[0]
    dateToSplit = dateToSplit[1].split('-', 1)
    month = dateToSplit[0]
    day = dateToSplit[1]
    return year, month, day

for i in range(1, 8):
    if(i == 1):
        d_date = str(datetime.date.today() + timedelta(days = 1))
        d_year, d_month, d_day = date_splitter(d_date)
        r_date = str(datetime.date.today() + timedelta(days = 31))
        r_year, r_month, r_day = date_splitter(r_date)
        #scrapeLink = 'https://www.expedia.de/Flights-Search?trip=roundtrip&leg1=from:Munich,%20Germany%20(MUC),to:Chennai,%20India%20(MAA),departure:17/06/2018TANYT&leg2=from:Chennai,%20India%20(MAA),to:Munich,%20Germany%20(MUC),departure:17/07/2018TANYT&passengers=adults:1,children:0,seniors:0,infantinlap:Y&options=cabinclass:economy&mode=search&origref=www.expedia.de'
        scrapeLink = 'https://www.expedia.de/Flights-Search?trip=roundtrip&leg1=from%3AMunich%2C%20Germany%20(MUC)%2Cto%3AChennai%2C%20India%20(MAA)%2Cdeparture%3A' + d_day + '%2F' + d_month + '%2F' + d_year + 'TANYT&leg2=from%3AChennai%2C%20India%20(MAA)%2Cto%3AMunich%2C%20Germany%20(MUC)%2Cdeparture%3A' + r_day + '%2F' + r_month + '%2F' + r_year + 'TANYT&passengers=adults%3A1%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.co.in'
        print(scrapeLink)
    elif(i == 2):
        d_date = str(datetime.date.today() + timedelta(days = 3))
        d_year, d_month, d_day = date_splitter(d_date)
        r_date = str(datetime.date.today() + timedelta(days = 33))
        r_year, r_month, r_day = date_splitter(r_date)
        scrapeLink = 'https://www.expedia.de/Flights-Search?trip=roundtrip&leg1=from%3AMunich%2C%20Germany%20(MUC)%2Cto%3AChennai%2C%20India%20(MAA)%2Cdeparture%3A' + d_day + '%2F' + d_month + '%2F' + d_year + 'TANYT&leg2=from%3AChennai%2C%20India%20(MAA)%2Cto%3AMunich%2C%20Germany%20(MUC)%2Cdeparture%3A' + r_day + '%2F' + r_month + '%2F' + r_year + 'TANYT&passengers=adults%3A1%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.de'
        print(scrapeLink)
    elif(i == 3):
        d_date = str(datetime.date.today() + timedelta(days = 7))
        d_year, d_month, d_day = date_splitter(d_date)
        r_date = str(datetime.date.today() + timedelta(days = 37))
        r_year, r_month, r_day = date_splitter(r_date)
        scrapeLink = 'https://www.expedia.de/Flights-Search?trip=roundtrip&leg1=from%3AMunich%2C%20Germany%20(MUC)%2Cto%3AChennai%2C%20India%20(MAA)%2Cdeparture%3A' + d_day + '%2F' + d_month + '%2F' + d_year + 'TANYT&leg2=from%3AChennai%2C%20India%20(MAA)%2Cto%3AMunich%2C%20Germany%20(MUC)%2Cdeparture%3A' + r_day + '%2F' + r_month + '%2F' + r_year + 'TANYT&passengers=adults%3A1%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.co.in'
        print(scrapeLink)
    elif(i == 4):
        d_date = str(datetime.date.today() + timedelta(days = 15))
        d_year, d_month, d_day = date_splitter(d_date)
        r_date = str(datetime.date.today() + timedelta(days = 45))
        r_year, r_month, r_day = date_splitter(r_date)
        scrapeLink = 'https://www.expedia.de/Flights-Search?trip=roundtrip&leg1=from%3AMunich%2C%20Germany%20(MUC)%2Cto%3AChennai%2C%20India%20(MAA)%2Cdeparture%3A' + d_day + '%2F' + d_month + '%2F' + d_year + 'TANYT&leg2=from%3AChennai%2C%20India%20(MAA)%2Cto%3AMunich%2C%20Germany%20(MUC)%2Cdeparture%3A' + r_day + '%2F' + r_month + '%2F' + r_year + 'TANYT&passengers=adults%3A1%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.de'
        print(scrapeLink)
    elif(i == 5):
        d_date = str(datetime.date.today() + timedelta(days = 30))
        d_year, d_month, d_day = date_splitter(d_date)
        r_date = str(datetime.date.today() + timedelta(days = 60))
        r_year, r_month, r_day = date_splitter(r_date)
        scrapeLink = 'https://www.expedia.de/Flights-Search?trip=roundtrip&leg1=from%3AMunich%2C%20Germany%20(MUC)%2Cto%3AChennai%2C%20India%20(MAA)%2Cdeparture%3A' + d_day + '%2F' + d_month + '%2F' + d_year + 'TANYT&leg2=from%3AChennai%2C%20India%20(MAA)%2Cto%3AMunich%2C%20Germany%20(MUC)%2Cdeparture%3A' + r_day + '%2F' + r_month + '%2F' + r_year + 'TANYT&passengers=adults%3A1%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.co.in'
        print(scrapeLink)
    elif(i == 6):
        d_date = str(datetime.date.today() + timedelta(days = 60))
        d_year, d_month, d_day = date_splitter(d_date)
        r_date = str(datetime.date.today() + timedelta(days = 90))
        r_year, r_month, r_day = date_splitter(r_date)
        scrapeLink = 'https://www.expedia.de/Flights-Search?trip=roundtrip&leg1=from%3AMunich%2C%20Germany%20(MUC)%2Cto%3AChennai%2C%20India%20(MAA)%2Cdeparture%3A' + d_day + '%2F' + d_month + '%2F' + d_year + 'TANYT&leg2=from%3AChennai%2C%20India%20(MAA)%2Cto%3AMunich%2C%20Germany%20(MUC)%2Cdeparture%3A' + r_day + '%2F' + r_month + '%2F' + r_year + 'TANYT&passengers=adults%3A1%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.de'
        print(scrapeLink)
    elif(i == 7):
        d_date = str(datetime.date.today() + timedelta(days = 90))
        d_year, d_month, d_day = date_splitter(d_date)
        r_date = str(datetime.date.today() + timedelta(days = 120))
        r_year, r_month, r_day = date_splitter(r_date)
        scrapeLink = 'https://www.expedia.de/Flights-Search?trip=roundtrip&leg1=from%3AMunich%2C%20Germany%20(MUC)%2Cto%3AChennai%2C%20India%20(MAA)%2Cdeparture%3A' + d_day + '%2F' + d_month + '%2F' + d_year + 'TANYT&leg2=from%3AChennai%2C%20India%20(MAA)%2Cto%3AMunich%2C%20Germany%20(MUC)%2Cdeparture%3A' + r_day + '%2F' + r_month + '%2F' + r_year + 'TANYT&passengers=adults%3A1%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.co.in'
        print(scrapeLink)

    ua1 = UserAgent()
    randomHeader = {'User-Agent':str(ua1.random)}
    page = requests.get(scrapeLink, randomHeader)
    soup = BeautifulSoup(page.content, 'html.parser')
    priceJson = soup.find_all('script', {'id': 'cachedResultsJson'})[0].get_text()
    parsed = json.loads(priceJson)
    skimData = parsed['content']
    skimData = json.loads(skimData)
    
    train = pd.DataFrame.from_dict(skimData['legs'], orient='index').reset_index()

    finalDf = pd.DataFrame()
    finalDf['naturalKey'] = train['naturalKey']
    finalDf['price'] = train['price']
    finalDf['carrierSummary'] = train['carrierSummary']

    x = finalDf['carrierSummary'].to_dict()
    y = finalDf['price'].to_dict()

    aList = list()
    pList = list()

    for i in range(len(x)):
        if(x[i]['airlineName'] == ''):
            z = 0
        else:
            aList.append(x[i]['airlineName'])
            pList.append(y[i]['exactPrice'])

    newDf = pd.DataFrame()

    newDf['airline'] = aList
    newDf['price'] = pList

    newDf = newDf[newDf['price'].isin(newDf.groupby('airline').min()['price'].values)]
    newDf = newDf.drop_duplicates(subset = ['airline', 'price'], keep = 'first')

    print(newDf)

    sleep(10)


end_time = time()

total_time = end_time - start_time

print('Execution time was', total_time, 'seconds')