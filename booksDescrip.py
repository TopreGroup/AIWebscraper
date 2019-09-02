from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import csv 
import re
import os
from lxml import html
from urllib.parse import urljoin

# url4 = "http://www.bairnsdalebookshop.com.au/a-navajo-sketch-book.html"
# url2 ="http://www.bairnsdalebookshop.com.au/arts-and-photography.html"
# url = "http://www.bairnsdalebookshop.com.au/biographies-and-memoirs.html"
# url3 ="http://www.bairnsdalebookshop.com.au/biographies-and-memoirs.html"
base ="http://www.bairnsdalebookshop.com.au"
# Url =url4



class bookDescrip():

    def __init__(self,base,url):
        self.base = base
        self.url = url



    def tearDown(self):
        data = urlopen(self.url)
        pageContent = data.read()
        soup = BeautifulSoup( pageContent,"lxml",from_encoding=data.info().get_param('charset'))
        prodLoc = [s.get_text(separator=";", strip=True) for s in soup.find_all("div",{"class":"breadcrumbs"})]


        #product title and Nav 

        for i in range(len(prodLoc)):
            text = str(prodLoc[i])
            prodTitle = text.split(";")[2]
            prodCat = text.split(";")[1]
            print("Prod location :",text, "ProdTitle:",prodTitle)
            # print(prodCat)

        # price of book 
        pTemp = [s.get_text(strip=True) for s in soup.find_all("span",{"class":"price"})]
        price=(str(pTemp[0])).split(":")[1]
        # print(pTemp)


        # Image concatenate with base url
        prodImage = soup.find_all("img",{"class":"cm-thumbnails"})
        prodImage = prodImage[0].get("src")
        prodImage = base+prodImage
        # print(prodImage)

        # Product description

        prodDescrip = soup.find_all("div",{"id":"content_block_description"})
        # print(len(prodDescrip))
        # print(prodDescrip)
        for i in range(len(prodDescrip)):
            descrip = prodDescrip[i].text
            descrip = descrip.strip()
            descrip = descrip.replace(".",";")
            # print(descrip)



        # Stock level

        stock = [s.get_text( strip=True) for s in soup.find_all("span",{"class":"strong in-stock"})]
        stock = stock[0]
        # print(stock)

        prodRow = [str(prodCat),str(text),str(prodTitle),str(descrip),str(price),str(prodImage),self.url,None]
        
        
        return prodRow
        # print(prodRow)


# url = "http://www.bairnsdalebookshop.com.au/a-kind-of-treason.html"
# run = bookDescrip(base,url)
# run.tearDown()
