from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import csv 
import re
import os
# import urllib2
from lxml import html
# 'https://www.budgetpc.com.au/networking/network-hardware/switches/non-poe-switches.html', 
# 'https://www.budgetpc.com.au/networking/network-hardware/switches/non-poe-switches.html?p=2',
#  'https://www.budgetpc.com.au/networking/network-hardware/switches/non-poe-switches.html?p=3', 
#  'https://www.budgetpc.com.au/networking/network-hardware/switches/non-poe-switches.html?p=4', 
#  'https://www.budgetpc.com.au/networking/network-hardware/switches/non-poe-switches.html?p=5']

# url ="https://www.budgetpc.com.au/computers-servers/ms-surface/surface-extended-warranty/surface-student-extended-warranty.html"

url = "https://www.budgetpc.com.au/"

#connect to a URL
# website = urlopen(url)
r = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c = r.content
soup = BeautifulSoup(c,"html.parser")
#read html code
# html = website.read()
text = soup.find_all("href")
print(text)
#use re.findall to get all the links
# links = re.findall('"((http|ftp)s?://.*?)"', text)

# extract link url from the anchor
for link in soup.find_all(‘a’):
    anchor = link.attrs[“href”] if “href” in link.attrs else ‘’





# a = a.replace("\n",",")
# href =[]
# for i in range((a.count(","))+1):
#     holder = a.split(",")[i]
#     href.append(holder)
# print(len(href))

