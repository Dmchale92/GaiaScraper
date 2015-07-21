__author__ = 'Quasi-Boden'
import time
import requests
import re
from bs4 import BeautifulSoup

minimumPrice = raw_input('Please enter minimum price:')
maximumPrice = raw_input('Please enter maximum price:')

print('Fetching Marketplace Items between ' + str(minimumPrice) + ' and ' + str(maximumPrice) + '...')
url = 'http://www.gaiaonline.com/marketplace/itemsearch/100/?search=&filter=0&showall=on&floor=' + str(minimumPrice) +'&ceiling=' + str(maximumPrice) + '&sortBy=85'
marketPage = requests.get(url)
print(url)


soup = BeautifulSoup(marketPage.content)
itemList = []

print('Building item list...')
for link in soup.find_all('div', 'sparkles_container'):
    itemList.append('http://www.gaiaonline.com' + link.a['href'])

for link in itemList:
    time.sleep(1)
    item = requests.get(link)
    soup = BeautifulSoup(item.content)
    textSoup = soup.get_text()
    lowestBuyFilter = re.compile(ur'Lowest Buy Now Price:\s*\S* ')
    lowestBuyPriceText = re.findall(lowestBuyFilter, textSoup)
    lowestBuyPrice = float(re.sub(r"\D", "", str(lowestBuyPriceText)))

    averageBuyFilter = re.compile(ur'Average Buy Price:\s*\S* ')
    averageBuyPriceText = re.findall(averageBuyFilter, textSoup)
    averageBuyPrice = float(re.sub(r"\D", "", str(averageBuyPriceText)))

    potentialProfit = averageBuyPrice / lowestBuyPrice * 100
    if potentialProfit > 150:
        print(link + ' : Potential Profit = ' + str(int(potentialProfit)) + '%')
