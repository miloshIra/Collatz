import requests
from bs4 import BeautifulSoup
import csv


request = requests.get('https://www.bookdepository.com/search?searchTerm=learning+python&search=Find+book')
content = request.content
list1 = []
list2 = []
soup = BeautifulSoup(content, 'html.parser')
title = soup.find_all('h3', attrs={'class':'title'})
price = soup.find_all('p', attrs={'class':'price'})

for title in title:
    name=title.text.strip()
    list1.append(name)

for price in price:
    string_price=(price.text.strip())
    price_whole_number = string_price[0:2]
    price_decimal = string_price[3:7]
    price_whole=(price_whole_number + "." + price_decimal)
    list2.append(price_whole)


k = list(zip(list1,list2))

for i in k:
        with open ('books.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([k])

print(k[2])


# https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
