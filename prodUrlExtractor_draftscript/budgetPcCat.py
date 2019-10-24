from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import csv 
import re
import os
from lxml import html

# https://www.budgetpc.com.au/817925-b21-hpe-dl380-gen9-e5-2609v4-processor-kit.html
# url = "https://www.budgetpc.com.au/computer-hardware.html"
# url = "https://www.budgetpc.com.au/computer-hardware.html"
# url ="https://www.budgetpc.com.au/computer-hardware/computer-components.html"
# url ="https://www.budgetpc.com.au/computer-hardware/computer-components/memory/sodimm-memory.html"
class budgetCat():
    
    def __init__(self, url):
        self.url = url

    def main (self):

        try:

            # r = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
            # c = r.content
            r = requests.get(self.url, headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
            c = r.content
            soup = BeautifulSoup(c,"html.parser")

            subUrls =[self.url]
            # nav pages 
            varNew = soup.find("div",{"class":"pages"})
            # print(varNew)
            subNav =varNew.findChildren()
            navUrl = []
            # print(len(subNav))
            # print(subNav[0].get("href"))
            for i in range(len(subNav)):
                if subNav[i].get("href") is not None:
                    holder = subNav[i].get("href")
                    navUrl.append(holder)
                    # print(holder)

            navUrl=list(dict.fromkeys(navUrl))
            subUrls.extend(navUrl)
            print(subUrls)


            levelOne = self.url.split("https://www.budgetpc.com.au/",1)[1]
            levelOne =levelOne.replace(".html","")
            if "/" in levelOne:
                leveltwo= levelOne
                levelOne = levelOne.split("/",1)[0]
                print("1",levelOne)
                print("2",leveltwo)

            else:
                leveltwo = ";"    



            prodUrl = []
            for i in range(len(subUrls)):
                holder = self.prodUrl(subUrls[i])
                print(len(holder),"product url in index: ",i)
                prodUrl.extend(holder)
                # print("cat sleep 3s")
                # time.sleep(3)


            print(len(prodUrl),"product Urls in Category: ", levelOne, "/",leveltwo)
            # return levelOne, leveltwo, prodUrl 
            return prodUrl        

        except:
            print("broken link")
            
            prodUrl = None

            return prodUrl


       
        

        # print(levelOne)

    def prodUrl(self, url):
        r = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
        c = r.content
        soup = BeautifulSoup(c,"html.parser")

        subProd = soup.find_all("div",{"class":"product-image-wrapper nohover"})

        # print((subProd[0].a).get("href"))
        # print(subProd[0])
        prodUrl = []
        # print(type(subProd))
        for i in range(len(subProd)):
            holder = (subProd[i].a).get("href")
            # holder = holder.get("href")
            if holder is not None:
                prodUrl.append(holder)
                # print(holder)
        # print(len(prodUrl))
        return prodUrl        

# # nav pages 
# subNav =soup.find("div",{"class":"pages"}).findChildren()
# navUrl = []
# print(len(subNav))
# print(subNav[0].get("href"))
# for i in range(len(subNav)):
#     if subNav[i].get("href") is not None:
#         holder = subNav[i].get("href")
#         navUrl.append(holder)
#         print(holder)

# navUrl=list(dict.fromkeys(navUrl))

# print(navUrl)


# # print(subNav)
# print(len(navUrl))
# print("navUrls...",len(navUrl))

# run = budgetCat(url)
# run.main()

# https://www.budgetpc.com.au/fkg-00007-microsoft-surface-pro-256gb-i7-8g-comm-m1796-sc-english-australia-new-zealand-1-license.html