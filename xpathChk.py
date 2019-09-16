import requests
from lxml import html, etree
import lxml.html
from html.parser import HTMLParser
from bs4 import BeautifulSoup, Comment
from urllib.request import urlopen as U
import requests
import re
import os
import time
from goose3 import Goose
 
# url = "https://www.knncomputers.com.au/collections/used-refurbished-cheap-laptops-of-hp-dell-lenovo/products/thinkpad-x250-laptop-i5-5300u-2-3ghz-4g-8g-128g-240g-500g-ssd-12-5in"
# Title = "Thinkpad X250 Laptop i5-5300U 2.3GHz 8G 256GB SSD 12.5in - 6Months RTB"
# url2 = "https://www.knncomputers.com.au/collections/lenovo-laptops/products/lenovo-thinkpad-x240-core-i7-4600u-8g-180g-ssd-wifi-12-5-w10p"
# Title2 = 'Lenovo ThinkPad X240 Core i7 4600U 8G 180G SSD WiFi 12.5" W10P'
# url3 ="https://www.budgetpc.com.au/sm-w700nzwaxsa-samsung-galaxy-tabpro-s-12-home-tablet-white.html"
# Title3 = 'Samsung - Samsung Galaxy TabPro S 12" Home Tablet - White'
# url4 ="https://www.reboot-it.com.au//p/Used-SmartPhones/Samsung/Samsung-Galaxy-S7-32GB-Mobile-Phone-Unlocked-Gold/31419-B"
# Title4 = 'Samsung Galaxy S7 32GB Mobile Phone Unlocked Gold | B Grade 6mth Wty'








def xpath(name, prodUrl, title):
    """Read url from txt and filters out Product Urls only
    
    Arguments:
        name {String} -- company name
        prodUrl {String} -- sample product url
        title {String} -- product title found on prod url
    """
    
    try:
        
        """Read company url text file and adds it to a set"""

        file1 = open(name+".txt","r+")  
        pattern = re.compile("^(http|https):\/\/")
        
        urls = set()
        for line in file1:
            line = file1.readline()
            line = line.strip()
            if not line:
                continue
            if pattern.match(line):
                holder= line
                urls.add(line)
                # print(line)
            # else :
            #     print(line)
        file1.close()


        """# Xpath extracting from produrl and title.Using sets to avoid duplicate"""

        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        page = requests.get(prodUrl, headers= headers)
        
        
        root = html.fromstring(page.text)
        tree = root.getroottree()
        title = "//*[. = '"+title+"']" 
        result = root.xpath(title)
        refPath = set()
        for r in result:
            holder = tree.getpath(r)
            refPath.add(holder)
            print(refPath)

        """typcasting set to list"""
        refPath = list(refPath)
        
        """Verifying title xpath on the same prodUrl, and creating a filtered xpath list"""
        refPathFilter = []
        treeHtml = html.fromstring(page.content)
        for i in range(len(refPath)):
            holder = str(refPath[i])+'/text()'
            titleChk = treeHtml.xpath(holder)
            if not titleChk:
                continue
            else:
                refPathFilter.append(str(refPath[i]))

        
        for url in urls:
            flag = 0
            prodUrls = set ()
            pageHolder = requests.get(url, headers= headers)
            treeHtml = html.fromstring(pageHolder.content)
            
            
        """Checking xpath content in all urls, if content exist url is a produrl"""
            for i in range(len(refPathFilter)):

                # if flag != 0:
                #     break

                # xtitle =str(refPathFilter[i])+'/text()'
                # element1 = treeHtml.xpath(xtitle)
                # if not element1 or len(element1)==0:
                #     flag +=1
                #     break
                
                # else:
                    
                #     print(xtitle)
                    
                #     element1 = str(element1[0])
                #     for j in range(len(refPathFilter)):
                #         ytitle = str(refPathFilter[j])+'/text()'
                #         element2 = treeHtml.xpath(ytitle)
                        
                #         if not element1 or len(element1)==0:
                #             flag += 1
                #             break

                #         if element1 != element2:
                #             flag += 1  
                #             break
                #         else:
                #             continue       
                xtitle =str(refPathFilter[i])+'/text()'
                print(xtitle)
                element1 = treeHtml.xpath(xtitle)
                print(element1)
                if len(element1)==0:
                    if i== len(refPathFilter)-1:
                        flag +=1
                        break
                else:
                    continue
            """writing produrl to a txt file"""
            
            if flag==0:
                row = str(url)
                file1 = open(name+"ProdUrl.txt","a")  
                file1.write( row +",\n") 
                file1.close()
            else:
                print("no! : " +url)     

    except:
        print("txt file not found")






# prodUrls = xpath(urls, url4, Title4)
