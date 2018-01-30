import requests, os, bs4

url = 'https://'   # starting URL
os.makedirs('Emily Heaven', exist_ok=True)                       # stores in Emily heaven

while not url.endswith('#'):

    print('Downloading image %s...' %url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "lxml")
    element = soup.select('#primary img')
    
    if element == []:

        print('Could not find image')

    else:
        elementUrl = element[0].get('src')
        res = requests.get(elementUrl)
        res.raise_for_status()

        imageFile = open(os.path.join('Emily Heaven', os.path.basename(elementUrl)), 'wb')
        for chunk in res.iter_content():
            imageFile.write(chunk)
        imageFile.close()



print('Done')


            
