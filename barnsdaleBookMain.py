from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import csv 
import re
import os

from lxml import html
from urllib.parse import urljoin
from booksCatlist import booksCat as bkCat
from booksDescrip import bookDescrip as bkdetail
import time
# pagination cm-pagination-wraper center

url = "http://www.bairnsdalebookshop.com.au"

data= urlopen(url)

pageContent = data.read()

soup= BeautifulSoup(pageContent, "lxml", from_encoding=data.info().get_param('charset'))

dropDownCat = soup.find_all( "ul", {"class":"dropdown dropdown-vertical"})
# print(len(dropDownCat))
dropDownCat = dropDownCat[0].find_all("a")
print(len(dropDownCat))
catUrl= [] #url list of catagories
catItem = [] #catagory items
for i in range(len(dropDownCat)):
    itemTitle = dropDownCat[i].text
    itemUrl = str(dropDownCat[i].get("href"))
    itemUrl = url+itemUrl
    catItem.append(itemTitle.strip())
    catUrl.append(itemUrl.strip())
    print("CatTitle:",itemTitle.strip(),"CatUrl:",itemUrl.strip())
print(len(catUrl),len(catItem))    

tempCatUrl = []
productUrl =[]
for i in range(len(catUrl)):
    holder  = catUrl[i]
    print(catItem[i], "-------Products in this Category")
    tempCatUrl = bkCat(url,holder).main()
    productUrl.extend(tempCatUrl)
    print("sleeping for 1 sec")
    time.sleep(1)
print("all pruductUrl",len(productUrl))


if os.path.exists('barnsdaleBook.csv') is False:
    row = ['Category', 'Sub Category', 'Product','Description','Price','Product Image','Product Url','Configuration']
    
    with open('barnsdaleBook.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()


for i in range(len(productUrl)):
    row = bkdetail(url,productUrl[i]).tearDown()
        
    with open('barnsdaleBook.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()
    print("sleep 2s")
    time.sleep(2)