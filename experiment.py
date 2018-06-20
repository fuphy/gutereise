from selenium import webdriver
from bs4 import BeautifulSoup as bs

url = 'https://www.skyscanner.net/transport/flights/muc/csha/180630/180730/?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=1&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&ref=home#results'
driver = webdriver.Firefox()
driver.get(url)
html = driver.execute_script("return document.body.innerHTML")
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
