from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import csv 
import re
import os
from lxml import html
from urllib.parse import urljoin
# Catalog links http://www.applebits.net/catalog/index.php
# Main Page http://www.applebits.net/
url = 'http://www.applebits.net/catalog/index.php?osCsid=dauds1f61mioio9g33trfhi1d6'
from CatList import scrapIt as ct 
from productList import scrapProduct as pl
from product import product as pd
import time


data= urlopen(url)

pageContent = data.read()

soup= BeautifulSoup(pageContent, "lxml", from_encoding=data.info().get_param('charset'))

# Find base url 
# base = soup.find("base").get("href")
# print(base)

# Page title
# title =soup.select("title")[0]
# print(title)
#########

# for link in soup.find_all("a", attrs={"href":re.compile("^http://")}):
#     link.append(link.get("href"))

# All links in a page
# for link in soup.find_all('a', href=True):
#     print(link['href'])
# # All product pages

# page structure for catalog
catalogs = soup.find_all( "td", {"class":"boxText"})
# print(type(catalogs))
catalog = catalogs[0].find_all("a")
print(len(catalog))
catUrl= [] #url list of catagories
catItem = [] #catagory items
for i in range(len(catalog)):
    itemTitile = str(catalog[i].text)
    itemTitile=re.sub('[^a-zA-Z0-9 \n\.]', '', itemTitile)
    catItem.append(itemTitile.strip())
    catUrl.append(str(catalog[i].get("href")))
    print(catUrl[i],"  ", catItem[i])


subCatUrl = [] 
subCatItem = []


for i in range(len(catUrl)):
    catLink=catUrl[i]
    #list containing al sub-cat and their title 
    
    tempCatUrl, tempCatItem = ct(catLink).scrap()
    # print(tempCatUrl)
    subCatUrl.extend(tempCatUrl)
    subCatItem.extend(tempCatItem)
  
print("beforepop")
print(len(subCatUrl)," ",len(subCatItem))   
    

print("beforepop")
print(len(subCatUrl)," ",len(subCatItem))  
for i in range(len(subCatUrl)):
    if subCatUrl[i]== url:
        subCatUrl.pop(i)
        subCatItem.pop(i)

print("afterpop")
print(len(subCatUrl)," ",len(subCatItem))

productUrl = []
productTitle = []
for i in range(len(subCatUrl)):
    tempLink = subCatUrl[i]
    # product link and title list (target links and title)
    
    tempProdUrl, tempProdTitle = pl(tempLink).scrapProducts()
    productUrl.extend(tempProdUrl)
    productTitle.extend(tempProdTitle)
    
# print(len(productUrl), ",",len(productTitle), "this is product list")

# Create CSV file with heading 
# row = ['Category', 'Sub Category', 'Product','Description','Price','Product Image','Product Url','Configuration']
# with open('appleBits.csv', 'a') as csvFile:
#     writer = csv.writer(csvFile)
#     writer.writerow(row)
# csvFile.close()



for i in range(len(productUrl)):
        row = pd(productUrl[i]).prodDetail()
        
        with open('appleBits.csv', 'a') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
        csvFile.close()
        print("sleep 2s")
        time.sleep(2)