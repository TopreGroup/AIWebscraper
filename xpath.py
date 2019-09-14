import requests
from lxml import html
 
from html.parser import HTMLParser
from bs4 import BeautifulSoup, Comment
from urllib.request import urlopen as U
import requests
import re
import os
import time
from goose3 import Goose
 
url = "https://www.knncomputers.com.au/collections/used-refurbished-cheap-laptops-of-hp-dell-lenovo/products/thinkpad-x250-laptop-i5-5300u-2-3ghz-4g-8g-128g-240g-500g-ssd-12-5in"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
title = "Thinkpad X250 Laptop i5-5300U 2.3GHz 8G 256GB SSD 12.5in - 6Months RTB"
 
page = requests.get(url)
root = html.fromstring(page.text)
tree = root.getroottree()
title = "//*[. = '"+title+"']"
result = root.xpath(title)
for r in result:
    print(tree.getpath(r))