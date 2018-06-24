from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent

url = 'https://www.skyscanner.net/transport/flights/muc/maa/180630/180730/?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=1&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&ref=home#results'
"""
driver = webdriver.Firefox()
driver.get(url)
html = driver.execute_script("return document.body.innerHTML")
driver.close() 
"""

profile = webdriver.FirefoxProfile()
ua1 = UserAgent()
profile.set_preference('general.useragent.override', str(ua1.random))
driver = webdriver.Firefox(profile)
driver.get(url)
delay = 30
while True:
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'airlines')))
        print('Page is ready!')
        break 
    except TimeoutException:
        print('Loading took too much time!')
html = driver.execute_script('return document.body.innerHTML')
driver.close()

b_html = bs(html,'html.parser') 
x = b_html.find_all('ol', class_='airlines')

aList = []
pList = []

for row in x:
    y = row.find_all('span', class_ = 'label-text')
    z = row.find_all('span', class_ = 'filter-sub')

    for i in range(len(y)):
        aList.append(y[i])
        pList.append(z[i])
        
for k in range(len(aList)):
    print(aList[k], 'available at', pList[k])