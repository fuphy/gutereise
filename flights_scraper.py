from time import time, sleep
import requests
from datetime import datetime, timedelta
import datetime
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json
import pandas as pd
from pandas import ExcelWriter

start_time = time()

def date_splitter(dateToSplit):
    dateToSplit = dateToSplit.split('-', 1)
    year = dateToSplit[0]
    dateToSplit = dateToSplit[1].split('-', 1)
    month = dateToSplit[0]
    day = dateToSplit[1]
    return year, month, day

xlsDf = pd.DataFrame()

for i in range(1, 8):
    if(i == 1):
        dayInAdvance = 1
        d_date = str(datetime.date.today() + timedelta(days = 1))
        d_year, d_month, d_day = date_splitter(d_date)
        r_date = str(datetime.date.today() + timedelta(days = 31))
        r_year, r_month, r_day = date_splitter(r_date)
        scrapeLink = 'https://www.expedia.de/Flights-Search?trip=roundtrip&leg1=from%3AMunich%2C%20Germany%20(MUC)%2Cto%3AChennai%2C%20India%20(MAA)%2Cdeparture%3A' + d_day + '%2F' + d_month + '%2F' + d_year + 'TANYT&leg2=from%3AChennai%2C%20India%20(MAA)%2Cto%3AMunich%2C%20Germany%20(MUC)%2Cdeparture%3A' + r_day + '%2F' + r_month + '%2F' + r_year + 'TANYT&passengers=adults%3A1%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.de'
        print('Scraping data from', scrapeLink)
    elif(i == 2):
        dayInAdvance = 3
        d_date = str(datetime.date.today() + timedelta(days = 3))
        d_year, d_month, d_day = date_splitter(d_date)
        r_date = str(datetime.date.today() + timedelta(days = 33))
        r_year, r_month, r_day = date_splitter(r_date)
        scrapeLink = 'https://www.expedia.de/Flights-Search?trip=roundtrip&leg1=from%3AMunich%2C%20Germany%20(MUC)%2Cto%3AChennai%2C%20India%20(MAA)%2Cdeparture%3A' + d_day + '%2F' + d_month + '%2F' + d_year + 'TANYT&leg2=from%3AChennai%2C%20India%20(MAA)%2Cto%3AMunich%2C%20Germany%20(MUC)%2Cdeparture%3A' + r_day + '%2F' + r_month + '%2F' + r_year + 'TANYT&passengers=adults%3A1%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.de'
        print('Scraping data from', scrapeLink)
    elif(i == 3):
        dayInAdvance = 7
        d_date = str(datetime.date.today() + timedelta(days = 7))
        d_year, d_month, d_day = date_splitter(d_date)
        r_date = str(datetime.date.today() + timedelta(days = 37))
        r_year, r_month, r_day = date_splitter(r_date)
        scrapeLink = 'https://www.expedia.de/Flights-Search?trip=roundtrip&leg1=from%3AMunich%2C%20Germany%20(MUC)%2Cto%3AChennai%2C%20India%20(MAA)%2Cdeparture%3A' + d_day + '%2F' + d_month + '%2F' + d_year + 'TANYT&leg2=from%3AChennai%2C%20India%20(MAA)%2Cto%3AMunich%2C%20Germany%20(MUC)%2Cdeparture%3A' + r_day + '%2F' + r_month + '%2F' + r_year + 'TANYT&passengers=adults%3A1%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.de'
        print('Scraping data from', scrapeLink)
    elif(i == 4):
        dayInAdvance = 15
        d_date = str(datetime.date.today() + timedelta(days = 15))
        d_year, d_month, d_day = date_splitter(d_date)
        r_date = str(datetime.date.today() + timedelta(days = 45))
        r_year, r_month, r_day = date_splitter(r_date)
        scrapeLink = 'https://www.expedia.de/Flights-Search?trip=roundtrip&leg1=from%3AMunich%2C%20Germany%20(MUC)%2Cto%3AChennai%2C%20India%20(MAA)%2Cdeparture%3A' + d_day + '%2F' + d_month + '%2F' + d_year + 'TANYT&leg2=from%3AChennai%2C%20India%20(MAA)%2Cto%3AMunich%2C%20Germany%20(MUC)%2Cdeparture%3A' + r_day + '%2F' + r_month + '%2F' + r_year + 'TANYT&passengers=adults%3A1%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.de'
        print('Scraping data from', scrapeLink)
    elif(i == 5):
        dayInAdvance = 30
        d_date = str(datetime.date.today() + timedelta(days = 30))
        d_year, d_month, d_day = date_splitter(d_date)
        r_date = str(datetime.date.today() + timedelta(days = 60))
        r_year, r_month, r_day = date_splitter(r_date)
        scrapeLink = 'https://www.expedia.de/Flights-Search?trip=roundtrip&leg1=from%3AMunich%2C%20Germany%20(MUC)%2Cto%3AChennai%2C%20India%20(MAA)%2Cdeparture%3A' + d_day + '%2F' + d_month + '%2F' + d_year + 'TANYT&leg2=from%3AChennai%2C%20India%20(MAA)%2Cto%3AMunich%2C%20Germany%20(MUC)%2Cdeparture%3A' + r_day + '%2F' + r_month + '%2F' + r_year + 'TANYT&passengers=adults%3A1%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.de'
        print('Scraping data from', scrapeLink)
    elif(i == 6):
        dayInAdvance = 60
        d_date = str(datetime.date.today() + timedelta(days = 60))
        d_year, d_month, d_day = date_splitter(d_date)
        r_date = str(datetime.date.today() + timedelta(days = 90))
        r_year, r_month, r_day = date_splitter(r_date)
        scrapeLink = 'https://www.expedia.de/Flights-Search?trip=roundtrip&leg1=from%3AMunich%2C%20Germany%20(MUC)%2Cto%3AChennai%2C%20India%20(MAA)%2Cdeparture%3A' + d_day + '%2F' + d_month + '%2F' + d_year + 'TANYT&leg2=from%3AChennai%2C%20India%20(MAA)%2Cto%3AMunich%2C%20Germany%20(MUC)%2Cdeparture%3A' + r_day + '%2F' + r_month + '%2F' + r_year + 'TANYT&passengers=adults%3A1%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.de'
        print('Scraping data from', scrapeLink)
    elif(i == 7):
        dayInAdvance = 90
        d_date = str(datetime.date.today() + timedelta(days = 90))
        d_year, d_month, d_day = date_splitter(d_date)
        r_date = str(datetime.date.today() + timedelta(days = 120))
        r_year, r_month, r_day = date_splitter(r_date)
        scrapeLink = 'https://www.expedia.de/Flights-Search?trip=roundtrip&leg1=from%3AMunich%2C%20Germany%20(MUC)%2Cto%3AChennai%2C%20India%20(MAA)%2Cdeparture%3A' + d_day + '%2F' + d_month + '%2F' + d_year + 'TANYT&leg2=from%3AChennai%2C%20India%20(MAA)%2Cto%3AMunich%2C%20Germany%20(MUC)%2Cdeparture%3A' + r_day + '%2F' + r_month + '%2F' + r_year + 'TANYT&passengers=adults%3A1%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.de'
        print('Scraping data from', scrapeLink)

    ua1 = UserAgent()
    randomHeader = {'User-Agent':str(ua1.random)}
    page = requests.get(scrapeLink, randomHeader)
    soup = BeautifulSoup(page.content, 'html.parser')
    priceJson = soup.find_all('script', {'id': 'cachedResultsJson'})[0].get_text()
    parsed = json.loads(priceJson)
    skimData = parsed['content']
    skimData = json.loads(skimData)
    
    finalDf = pd.DataFrame.from_dict(skimData['legs'], orient='index').reset_index()
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
    newDf = newDf[newDf['price'].isin(newDf.groupby('airline').min()['price'].values)].reset_index()
    newDf = newDf.drop_duplicates(subset = ['airline', 'price'], keep = 'first').reset_index()
    newDf['scraperDate'] = str(datetime.date.today())
    newDf['departDate'] = d_date
    newDf['returnDate'] = r_date
    newDf['dayInAdvance'] = dayInAdvance
    newDf['departMonth'] = d_month
    newDf['returnMonth'] = r_month
    newDf['departMonth'] = newDf['departMonth'].map({'01': 'January', '02': 'February', '03': 'March', 
                            '04': 'April', '05': 'May', '06': 'June', '07': 'July', '08': 'August', 
                            '09': 'September', '10': 'October', '11': 'November', '12': 'December'})
    newDf['returnMonth'] = newDf['returnMonth'].map({'01': 'January', '02': 'February', '03': 'March', 
                            '04': 'April', '05': 'May', '06': 'June', '07': 'July', '08': 'August', 
                            '09': 'September', '10': 'October', '11': 'November', '12': 'December'})
    newDf.drop(newDf.columns[[0, 1]], axis = 1, inplace = True)
    print(newDf)
    xlsDf = xlsDf.append(newDf, ignore_index = True)
    sleep(60)

c_date = str(datetime.date.today())
c_year, c_month, c_day = date_splitter(c_date)

file_name = 'data/' + c_year + c_month + c_day + '_muc_maa.xlsx'
writer = pd.ExcelWriter(file_name, engine = 'xlsxwriter')
xlsDf.to_excel(writer, index = False, sheet_name = 'Sheet1')
writer.save()

end_time = time()

total_time = end_time - start_time

print('Execution time was', total_time, 'seconds')