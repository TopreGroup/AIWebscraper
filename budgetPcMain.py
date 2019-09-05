from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import csv 
import re
import os
from lxml import html
from budgetPcCat import budgetCat as bc
from budgetProdDescrip import budgetProd as bd 
import time


r = requests.get("https://www.budgetpc.com.au/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c = r.content

soup = BeautifulSoup(c,"html.parser")


dropDownCat = soup.find( "div", {"class":"span12"}).findChildren()
# print(type(dropDownCat))
# print(len(dropDownCat))
temp =[]
href =[]
for i in range(len(dropDownCat)):
    holder = dropDownCat[i].get("href")
    if holder is not None and "html" in holder:
        href.append(holder)
      
# print(len(href))

# for i in range(len(href)):
#     row = href[i]
#     file1 = open("href.txt","a")    
#     file1.write( row+"\n") 
#     file1.close() 
# # File_object = open(r"hrefs","Access_Mode")       

prodUrl = []
prodList = []
count = 0
for i in range(len(href)):
    holder = href[i]

    levelOne, levelTwo, holdertwo = bc(holder).main()
    count = count+len(holdertwo)
    prodUrl.extend(holdertwo)
    for i in range(len(holdertwo)):
        holderThree = bd(levelOne,levelTwo,holdertwo[i]).main()
        prodList.extend(holderThree)
        print("sleep 1s")
        time.sleep(1)

print("Final Product list count:", count)
if os.path.exists('budgetPc.csv') is False:
    row = ['Category', 'Sub Category', 'Product','Description','Price','Product Image','Product Url','Configuration']
    
    with open('budgetPc.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()


for i in range(len(prodList)):
    row = prodlist[i]
        
    with open('budgetPc.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()
    

# print(href[0])