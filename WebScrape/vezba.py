import urllib.request
from bs4 import BeautifulSoup
import csv
from datetime import datetime

quote_page = ['https://www.bloomberg.com/quote/SPX:IND','http://www.bloomberg.com/quote/CCMP:IND']

data=[]

for pg in quote_page:
    page=urllib.request.urlopen(pg)
    soup=BeautifulSoup(page, 'html.parser')
    name_box = soup.find('h1', attrs={'class':'name'})
    name=name_box.text.strip() # strip is used to remove starting and trailing
    print(name)

    price_box = soup.find('div', attrs={'class':'price'})
    price=price_box.text
    print(price)
    data.append((name,price))

# open a csv file with append, so old data will be erased
with open ('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    for name, price in data:
        writer.writerow([name, price, datetime.now()])


# https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
