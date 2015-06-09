__author__ = 'Quasi-Boden'

import requests
from bs4 import BeautifulSoup

minimumPrice = raw_input('Please enter minimum price:')
maximumPrice = float(minimumPrice) * 1.1

url = 'http://www.gaiaonline.com/marketplace/itemsearch/100/?search=&filter=0&showall=on&floor=' + str(minimumPrice) +'&ceiling=' + str(maximumPrice) + '&sortBy=85'
marketPage = requests.get(url)

soup = BeautifulSoup(marketPage.content)
#print(BeautifulSoup.prettify(soup))
print(url)
import re

itemList = []

for link in soup.find_all('div', 'sparkles_container'):
    itemList.append('http://www.gaiaonline.com/' + link.a['href'])

#for link in itemList:
#    item = requests.get(link)
#    soup = BeautifulSoup(item.content)
#    print(soup.find_all('Average Buy Price:'))


test_url = 'http://www.gaiaonline.com//marketplace/itemdetail/10022863'
item = requests.get(test_url)
soup = BeautifulSoup(item.content)
print(soup.find(id='item_basicdata').find('gold'))
print(soup.find_all(re.compile('/[0-9]*\sgold/')))