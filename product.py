from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import csv
import re
import os
from lxml import html
from urllib.parse import urljoin

url = "http://www.applebits.net/catalog/product_info.php?products_id=932&osCsid=48tqsqsoa4t0gdgh8vc8lotmr1"
url2="http://www.applebits.net/catalog/product_info.php?products_id=926&osCsid=jju4acjkt8t7q0dkceg8iti0k7"
url3="http://www.applebits.net/catalog/product_info.php?cPath=2_24&products_id=334" 

# class product():

#     def __init__(self,url):
#         self.url = url 

data= urlopen(url3)
pageContent = data.read()
soup= BeautifulSoup(pageContent, "lxml", from_encoding=data.info().get_param('charset'))
# subProducts = soup.find_all("td", {"class": ["infoBoxContetns", "productListing-data", "smallText"]})
productNav = soup.find_all("td",{"class":"headerNavigation"})
soup= BeautifulSoup(pageContent, "lxml", from_encoding=data.info().get_param('charset'))
# product image 
image = soup.find_all('img', {'src' : re.compile(r'^(?=.*http)(?=.*(png|jpe?g)).*$')})


# soup.find_all("a", attrs={"href":re.compile("^http://")}):
# products location in page
# text = (productNav[0].text).strip()
# text = re.sub('[^a-zA-Z0-9 /\n\.]', ',', text)
# text = text.replace(" ","")
# text = text.replace("Top,Catalog,","")
# print(text)
# print(type(image))

# price and title
# title = soup.find_all("td",{"class":["pageHeading","productSpecialPrice"]})
# print(len(title))
# prodName = title[0].text
# price = title[1].text
# price=price.replace(" ","")
# print(price)
# if price.count("$")==2:
#     price=price.split("$",2)[2]
#     print("$"+price)
# else:
#     print(price)

# print(price,",",prodName)


# image url
# for i in range(len(image)):
#     temptitle = image[i].get("src")
#     print(type(temptitle))
#     print(temptitle)

# Description
description=soup.find_all("p")

print(len(description))

for i in range(len(description)):
    print(description[i])