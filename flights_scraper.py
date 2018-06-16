from time import time
import requests
from fake_useragent import UserAgent
from datetime import datetime, timedelta
import datetime

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
        d_days_1 = str(datetime.date.today() + timedelta(days = 1))
        d_year, d_month, d_day = date_splitter(d_days_1)
    elif(i == 2):
        days_3 = str(datetime.date.today() + timedelta(days = 3))
        print('Scrape from ', days_3)
    elif(i == 3):
        days_7 = str(datetime.date.today() + timedelta(days = 7))
        print('Scrape from ', days_7)
    elif(i == 4):
        days_15 = str(datetime.date.today() + timedelta(days = 15))
        print('Scrape from ', days_15)
    elif(i == 5):
        days_30 = str(datetime.date.today() + timedelta(days = 30))
        print('Scrape from ', days_30)
    elif(i == 6):
        days_60 = str(datetime.date.today() + timedelta(days = 60))
        print('Scrape from ', days_60)
    elif(i == 7):
        days_90 = str(datetime.date.today() + timedelta(days = 90))
        print('Scrape from ', days_90)




end_time = time()

total_time = end_time - start_time

print('Execution time was', total_time, 'seconds')