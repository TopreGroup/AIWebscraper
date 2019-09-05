from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import csv 
import re
import os
from lxml import html
# from selenium import webdriver



class budgetProd():
    
    def __init__(self, levelOne, LevelTwo, url):
        self.levelOne = levelOne
        self.LevelTwo = LevelTwo
        self.url = url


    def main(self):
        r = requests.get(self.url, headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
        c = r.content

        soup = BeautifulSoup(c,"html.parser")
        
        try:

            # prod nav
            prodNav = [s.get_text( strip=True) for s in soup.find_all("div",{"class":"breadcrumbs"})]

            prodNav = prodNav[0]
            prodNav = prodNav.replace("›",";")
            
            self.LevelTwo = self.LevelTwo.replace("/",";")
            prodNav = prodNav.replace(";",self.LevelTwo)
            # print(prodNav)

            # image
            prodImage = prodNav = soup.find_all("div",{"class":"product-image"})

            # print(prodImage)
            imageHolder = prodImage[0].img
            imageHolder = imageHolder.get("src")

            prodTitle = [s.get_text( strip=True) for s in soup.find_all("div",{"class":"product-name"})]
            prodTitle = prodTitle[0]

            # Price
            prodPrice = [s.get_text( strip=True) for s in soup.find_all("div",{"class":"price-box"})]

            if "Special Price" in str(prodPrice[0]):
                prodPrice = str(prodPrice[0]).split("$")[2]
                prodPrice = "$"+prodPrice
            else:
                prodPrice=prodPrice[0]


            # Product descript 
            prodDescrip = [s.get_text( strip=True) for s in soup.find_all("div",{"class":"short-description"})]
            prodDescrip = prodDescrip[0]
            
            prodDetail = [self.levelOne,prodNav,prodDescrip,prodPrice,imageHolder,self.url,None]
        except:
            print("sorry link is broken ")   
            prodDetail = [None,None,None,None,None,None,None]

        return prodDetail



# Not special price
# url ="https://www.budgetpc.com.au/catalog/product/view/id/79683/s/rz07-02270100-r3m1-razer-rz07-02270100-r3m1-tartarus-v2-mecha-membrane-gaming-keypad/"



# run = budgetProd(url)
# run.main()

