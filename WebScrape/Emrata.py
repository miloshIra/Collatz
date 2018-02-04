import urllib.request, urllib
from bs4 import BeautifulSoup
import os

qpage='https://xhamster.com/photos/gallery/emily-ratajkowski-mega-collection-1002080/'
os.makedirs('Pictures', exist_ok=True)

l=[]

for x in range(1,7):
    cur_page=qpage + str(x)
    page=urllib.request.urlopen(cur_page)
    soup=BeautifulSoup(page, "html.parser")
    image=soup.find_all('div', attrs={'class':'image-thumb'})
    print(image)

    for item in image:
        photo=item.get('data-lazy')
        print(photo)
        image_name = photo.split("/")[-1]
        urllib.request.urlretrieve(photo, "./Pictures/" + image_name)

#python download image from urll


    # imageFile = open(os.path.join('Pics', os.path.basename(photo)), 'wb')
    # for chunk in photo.iter_content():
    #     imageFile.write(chunk)
    # imageFile.close()

# imageFile = open(os.path.join('Pics', os.path.basename(photo)), 'wb')
# imageFile.write(photo)



# div=soup.find_all("ul", {"class":"photos page-list"})
# print(div)
# #element=soup.select('img src')
# #print(len(element))
