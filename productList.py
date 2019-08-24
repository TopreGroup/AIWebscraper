from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import csv 
import re
import os
from lxml import html






# /html/body/table[3]/tbody/tr/td[2]/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[6]

# print(len(subCats))

class scrapProduct():

    def __init__(self, url):
        self.url = url

    def scrapProducts(self):

        data= urlopen(self.url)
        pageContent = data.read()
        soup= BeautifulSoup(pageContent, "lxml", from_encoding=data.info().get_param('charset'))
        subProducts = soup.find_all("td", {"class": ["infoBoxContetns", "productListing-data", "smallText"]})
        soup= BeautifulSoup(pageContent, "lxml", from_encoding=data.info().get_param('charset'))

        subProduct = []

        for i in range(len(subProducts)):
            subProduct.extend(subProducts[i].find_all("a"))

        # print(len(subProduct))
        subProdUrl = []
        subProdTitle = []

        for i in range(len(subProduct)):

            itemHead = str(subProduct[i].text)
            itemHead=re.sub('[^a-zA-Z0-9 \n\.]', '', itemHead)
            itemHead = itemHead.strip()
            hrefs = str(subProduct[i].get("href"))
            # print(hrefs,",",itemHead)
            if len(itemHead) != 0:
                result=hrefs.find('product')
                if result != -1 :
                    subProdUrl.append(hrefs)
                    subProdTitle.append(itemHead)
                    print(hrefs,",",itemHead)  
        return subProdUrl, subProdTitle




# url = "http://www.applebits.net/catalog/index.php?cPath=50_66&osCsid=sm833mctiuba6ouv11449mqb55"

# run = scrapProduct(url)
# run.scrapProducts()
