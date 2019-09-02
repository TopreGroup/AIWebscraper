from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import csv 
import re
import os
from lxml import html
from urllib.parse import urljoin

# url = "http://www.bairnsdalebookshop.com.au/sport.html"
url ="http://www.bairnsdalebookshop.com.au/biographies-and-memoirs.html"
base = "http://www.bairnsdalebookshop.com.au"
class booksCat():

    def __init__(self, baseUrl,catUrl):
        self.baseUrl = baseUrl
        self.catUrl = catUrl


    def main(self):
        data = urlopen(self.catUrl)
        pageContent = data.read()
        soup = BeautifulSoup( pageContent,"lxml",from_encoding=data.info().get_param('charset'))
        # subUrl = soup.find_all( "a", {"class":"product-title"})
        pageNo = soup.find_all("a",{"class":"cm-history cm-ajax"})
        
        # subCatNavUrl = [self.catUrl]
        productUrl =[]
        if len(pageNo)!=0:
            print("Pages in this Category ",len(pageNo)+1)
            tempProductUrl = self.getProductUrl(self.catUrl)
            productUrl.extend(tempProductUrl)

            for i in range(len(pageNo)):
                holder = self.baseUrl+str(pageNo[i].get("href"))

                tempProductUrl = self.getProductUrl(holder)
                
                productUrl.extend(tempProductUrl)
                # print(holder)
            print(len(productUrl), "product Url length")       

        else:
            # print("only 1 page ")
            # holder = self.baseUrl+str(pageNo[i].get("href"))
            print("Pages in this Category ",len(pageNo)+1)
            tempProductUrl = self.getProductUrl(self.catUrl)
            productUrl.extend(tempProductUrl)
            print(len(tempProductUrl), "product Url length")
        return productUrl


        
        
    
    def getProductUrl(self,navUrl):
        data = urlopen(navUrl)
        pageContent = data.read()
        soup = BeautifulSoup( pageContent,"lxml",from_encoding=data.info().get_param('charset'))
        subUrl = soup.find_all( "a", {"class":"product-title"})
        tempSubUrl =[]

        for i in range(len(subUrl)):
            holder = subUrl[i].get('href')
            tempSubUrl.append(holder)

        # print(len(tempSubUrl))
        productUrl =[]
        for i in range(len(tempSubUrl)):
            holder = self.baseUrl+str(tempSubUrl[i])
            productUrl.append(holder)
            print(holder)

        return productUrl




# run = booksCat(base,url)
# run.main()


