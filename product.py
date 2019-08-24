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

class product():

    def __init__(self,url):
        self.url = url 

    def prodDetail(self):
        data= urlopen(self.url)
        pageContent = data.read()
        soup= BeautifulSoup(pageContent, "lxml", from_encoding=data.info().get_param('charset'))
        productNav = soup.find_all("td",{"class":"headerNavigation"})
        soup= BeautifulSoup(pageContent, "lxml", from_encoding=data.info().get_param('charset'))
   
        # product image 
        tempImage = soup.find_all('img', {'src' : re.compile(r'^(?=.*http)(?=.*(png|jpe?g)).*$')})
        # print(image)
        # image url
        for i in range(len(tempImage)):
            imageUrl = tempImage[i].get("src")
        #print(type(temptitle))
            # print("Image URL : ",imageUrl)
  
        # soup.find_all("a", attrs={"href":re.compile("^http://")}):
        # products location in page
        text = (productNav[0].text).strip()
        text = re.sub('[^a-zA-Z0-9 /\n\.]', ',', text)
        text = text.replace(" ","")
        catNav = text.replace("Top,Catalog,","")
        catNav = catNav.replace(",",";")
        Category = catNav.replace(";",",",1)
        Category = Category.split(",")[0]
        # print(Category)
        print(catNav)
        # print(catNav)
        
        # price and title
        title = soup.find_all("td",{"class":["pageHeading","productSpecialPrice"]})
        # print(len(title))
        prodName = title[0].text
        price = title[1].text
        price=price.replace(" ","")
        
        # print(price)
        if price.count("$")==2:
            
            price=price.split("$",2)[2]
            
            price=("$"+price)
            print("Price:",price,",","Product title: ",prodName)
        else:
            # print(price)
            print("Price:",price,",","Product title: ",prodName)
        # Description
        description=soup.find_all("p")
        descripText = description[len(description)-1].text
        # Cleaning description text 
        descripText = descripText.replace("  ", "")

        descripText = descripText.replace("* ", "",1)
        descripText = descripText.replace("* ", ";")

        descripText=re.sub('\s*\n\s*', '', descripText)
        # print(descripText)
        prodDetailList = [Category,catNav,prodName,descripText,price,imageUrl,self.url,None] 
        print(prodDetailList)
        return  prodDetailList  


run = product(url3)
run.prodDetail()