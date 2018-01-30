import urllib.request
from bs4 import BeautifulSoup
import os

qpage='https://xhamster.com/photos/gallery/emily-ratajkowski-mega-collection-1002080'
page=urllib.request.urlopen(qpage)


soup=BeautifulSoup(page, "html.parser")
# print(soup)
image=soup.find_all('a', attrs={'class':'photo-container photo-thumb'})



for item in image:
    item(str)
    photo=item.get('href')
    print(photo)

    imageFile = open(os.path.join('Pics', os.path.basename(photo)), 'wb')
    for chunk in photo.iter_content():
        imageFile.write(chunk)
    imageFile.close()

# imageFile = open(os.path.join('Pics', os.path.basename(photo)), 'wb')
# imageFile.write(photo)



# div=soup.find_all("ul", {"class":"photos page-list"})
# print(div)
# #element=soup.select('img src')
# #print(len(element))
