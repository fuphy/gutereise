from time import time, sleep
from datetime import datetime, timedelta
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from fake_useragent import UserAgent
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

xlsDf = pd.DataFrame()

for i in range(1, 8):
    if(i == 1):
        dayInAdvance = 1
        d_date = str(datetime.date.today() + timedelta(days = 1))
        d_year, d_month, d_day = date_splitter(d_date)
        r_date = str(datetime.date.today() + timedelta(days = 31))
        r_year, r_month, r_day = date_splitter(r_date)
        scrapeLink = 'https://flight.yatra.com/air-search-ui/int2/trigger?type=R&viewName=normal&flexi=0&noOfSegments=2&origin=MUC&originCountry=DE&destination=MAA&destinationCountry=IN&flight_depart_date=' + d_day + '/' + d_month + '/' + d_year + '&arrivalDate=' + r_day + '/' + r_month + '/' + r_year + '&ADT=1&CHD=0&INF=0&class=Economy&source=fresco-home&version=1.1'
        print('Scraping data from', scrapeLink)
    elif(i == 2):
        dayInAdvance = 3
        d_date = str(datetime.date.today() + timedelta(days = 3))
        d_year, d_month, d_day = date_splitter(d_date)
        r_date = str(datetime.date.today() + timedelta(days = 33))
        r_year, r_month, r_day = date_splitter(r_date)
        scrapeLink = 'https://flight.yatra.com/air-search-ui/int2/trigger?type=R&viewName=normal&flexi=0&noOfSegments=2&origin=MUC&originCountry=DE&destination=MAA&destinationCountry=IN&flight_depart_date=' + d_day + '/' + d_month + '/' + d_year + '&arrivalDate=' + r_day + '/' + r_month + '/' + r_year + '&ADT=1&CHD=0&INF=0&class=Economy&source=fresco-home&version=1.1'
        print('Scraping data from', scrapeLink)
    elif(i == 3):
        dayInAdvance = 7
        d_date = str(datetime.date.today() + timedelta(days = 7))
        d_year, d_month, d_day = date_splitter(d_date)
        r_date = str(datetime.date.today() + timedelta(days = 37))
        r_year, r_month, r_day = date_splitter(r_date)
        scrapeLink = 'https://flight.yatra.com/air-search-ui/int2/trigger?type=R&viewName=normal&flexi=0&noOfSegments=2&origin=MUC&originCountry=DE&destination=MAA&destinationCountry=IN&flight_depart_date=' + d_day + '/' + d_month + '/' + d_year + '&arrivalDate=' + r_day + '/' + r_month + '/' + r_year + '&ADT=1&CHD=0&INF=0&class=Economy&source=fresco-home&version=1.1'
        print('Scraping data from', scrapeLink)
    elif(i == 4):
        dayInAdvance = 15
        d_date = str(datetime.date.today() + timedelta(days = 15))
        d_year, d_month, d_day = date_splitter(d_date)
        r_date = str(datetime.date.today() + timedelta(days = 45))
        r_year, r_month, r_day = date_splitter(r_date)
        scrapeLink = 'https://flight.yatra.com/air-search-ui/int2/trigger?type=R&viewName=normal&flexi=0&noOfSegments=2&origin=MUC&originCountry=DE&destination=MAA&destinationCountry=IN&flight_depart_date=' + d_day + '/' + d_month + '/' + d_year + '&arrivalDate=' + r_day + '/' + r_month + '/' + r_year + '&ADT=1&CHD=0&INF=0&class=Economy&source=fresco-home&version=1.1'
        print('Scraping data from', scrapeLink)
    elif(i == 5):
        dayInAdvance = 30
        d_date = str(datetime.date.today() + timedelta(days = 30))
        d_year, d_month, d_day = date_splitter(d_date)
        r_date = str(datetime.date.today() + timedelta(days = 60))
        r_year, r_month, r_day = date_splitter(r_date)
        scrapeLink = 'https://flight.yatra.com/air-search-ui/int2/trigger?type=R&viewName=normal&flexi=0&noOfSegments=2&origin=MUC&originCountry=DE&destination=MAA&destinationCountry=IN&flight_depart_date=' + d_day + '/' + d_month + '/' + d_year + '&arrivalDate=' + r_day + '/' + r_month + '/' + r_year + '&ADT=1&CHD=0&INF=0&class=Economy&source=fresco-home&version=1.1'
        print('Scraping data from', scrapeLink)
    elif(i == 6):
        dayInAdvance = 60
        d_date = str(datetime.date.today() + timedelta(days = 60))
        d_year, d_month, d_day = date_splitter(d_date)
        r_date = str(datetime.date.today() + timedelta(days = 90))
        r_year, r_month, r_day = date_splitter(r_date)
        scrapeLink = 'https://flight.yatra.com/air-search-ui/int2/trigger?type=R&viewName=normal&flexi=0&noOfSegments=2&origin=MUC&originCountry=DE&destination=MAA&destinationCountry=IN&flight_depart_date=' + d_day + '/' + d_month + '/' + d_year + '&arrivalDate=' + r_day + '/' + r_month + '/' + r_year + '&ADT=1&CHD=0&INF=0&class=Economy&source=fresco-home&version=1.1'
        print('Scraping data from', scrapeLink)
    elif(i == 7):
        dayInAdvance = 90
        d_date = str(datetime.date.today() + timedelta(days = 90))
        d_year, d_month, d_day = date_splitter(d_date)
        r_date = str(datetime.date.today() + timedelta(days = 120))
        r_year, r_month, r_day = date_splitter(r_date)
        scrapeLink = 'https://flight.yatra.com/air-search-ui/int2/trigger?type=R&viewName=normal&flexi=0&noOfSegments=2&origin=MUC&originCountry=DE&destination=MAA&destinationCountry=IN&flight_depart_date=' + d_day + '/' + d_month + '/' + d_year + '&arrivalDate=' + r_day + '/' + r_month + '/' + r_year + '&ADT=1&CHD=0&INF=0&class=Economy&source=fresco-home&version=1.1'
        print('Scraping data from', scrapeLink)

    profile = webdriver.FirefoxProfile()
    ua1 = UserAgent()
    profile.set_preference('general.useragent.override', str(ua1.random))
    driver = webdriver.Firefox(profile)
    driver.get(scrapeLink)
    html = driver.execute_script('return document.body.innerHTML')
    driver.close() 

    b_html = BeautifulSoup(html,'html.parser') 
    air = b_html.find_all('span', class_='clip-overflow')
    rs = b_html.find_all('span', class_='filter-price')

    aList = []
    pList = []

    for i in range(len(air)):
        a = airline_extractor(str(air[i]))
        aList.append(a)
        p = price_extractor(str(rs[i]))
        pList.append(p)

    newDf = pd.DataFrame()
    newDf['airline'] = aList
    newDf['price'] = pList
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
    print(newDf)
    xlsDf = xlsDf.append(newDf, ignore_index = True)
    sleep(300)

c_date = str(datetime.date.today())
c_year, c_month, c_day = date_splitter(c_date)

file_name = 'data/' + c_year + c_month + c_day + '_sky_muc_maa.xlsx'
writer = pd.ExcelWriter(file_name, engine = 'xlsxwriter')
xlsDf.to_excel(writer, index = False, sheet_name = 'Sheet1')
writer.save()

end_time = time()

total_time = end_time - start_time

print('Execution time was', total_time, 'seconds')