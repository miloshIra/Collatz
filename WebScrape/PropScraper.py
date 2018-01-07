import requests
from bs4 import BeautifulSoup
import os
import pandas

r=requests.get("http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c=r.content

soup=BeautifulSoup(c,"html.parser")
all=soup.find_all("div",{"class":"propertyRow"})
all[0].find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")

page_nr=soup.find_all("a",{"class":"Page"})[-1].text
print(page_nr,"number of pages were found")

l=[]
base_url="http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
for page in range(0,int(page_nr)*10,10):
    print( )
    r=requests.get(base_url+str(page)+".html")
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    all=soup.find_all("div",{"class":"propertyRow"})

    for i in all:
        d={}
        d["Price"]=i.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")
        d["Address"]=i.find_all("span",{"class":"propAddressCollapse"})[0].text
        d["Locality"]=i.find_all("span",{"class":"propAddressCollapse"})[1].text
        try:
            d["Beds"]=i.find("span",{"class":"infoBed"}).find("b").text #(i.find("span",{"class":infoBed"}).find("b").text)) - For only geting the number of beds.
        except:
            d["Beds"]=None
        try:
            d["Area"]=i.find("span",{"class":"infoSqFt"}).find("b").text
        except:
            d["Area"]=None
        try:
            d["Full Baths"]=i.find("span",{"class":"infoValueFullBath"}).find("b").text
        except:
            d["Full Baths"]=None
        try:
            d["Half Baths"]=i.find("span",{"class":"infoValueHalfBath"}).find("b").text
        except:
            d["Half Baths"]=None

        for column_group in i.find_all("div",{"class":"columnGroup"}):

            for feature_group, feature_name in zip(column_group.find_all("span",{"class":"featureGroup"}),column_group.find_all("span",{"class":"featureName"})):

                if "Lot Size" in feature_group.text:
                    d["Lot Size"]=(feature_name.text)
        print(d)
        l.append(d)

df=pandas.DataFrame(l)
df.to_csv("Realestate.csv")
