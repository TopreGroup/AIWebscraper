from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import csv
import re
import os
from lxml import html
from urllib.parse import urljoin


class scrapIt():

    def __init__(self, url):
        self.url = url

    def scrap(self):

        data = urlopen(self.url)
        pageContent = data.read()
        soup = BeautifulSoup( pageContent,"lxml",from_encoding=data.info().get_param('charset'))
        subCats = soup.find_all("td", {"class": ["infoBoxContetns", "productListing-data", "smallText"]})
        # print(subCats)
        subCat= []
        for i in range(len(subCats)):
            subCat.extend(subCats[i].find_all("a"))


        subCatUrl = []  # url list of catagories
        subCatItem = []  # catagory items
            
        # print(len(subCat))
        # print(len(subCat),"pointer")
        # iterates over sub-Category of a tags 
        for i in range(len(subCat)):
            
            itemHead = str(subCat[i].text)
            itemHead=re.sub('[^a-zA-Z0-9 \n\.]', '', itemHead)
            itemHead = itemHead.strip()
            hrefs = str(subCat[i].get("href"))
            
          
            # ignore sets of empty text and product pages,returns list of url and corresponding text
            if len(itemHead) != 0:
                result=hrefs.find('product')
                if result != -1 :
                    continue
                else:
                    subCatUrl.append(hrefs)
                    subCatItem.append(itemHead)
                    # print(hrefs,",",itemHead)         
        # print(len(subCatUrl)," ",len(subCatItem))
        return subCatUrl, subCatItem
    
   

              

# url ="http://www.applebits.net/catalog/index.php?cPath=173&osCsid=sj32krlcgj40h3u253t49ie2f5"
# url2 = "http://www.applebits.net/catalog/index.php?cPath=2&osCsid=jv0qau5r89islf25fhed0fj4i4"

# run = scrapIt(url2)
# run.scrap()
