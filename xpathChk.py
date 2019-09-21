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
# from goose3 import Goose


def xpath(name, prodUrl, title):
    """Read url from txt and filters out Product Urls only

    Arguments:
        name {String} -- company name
        prodUrl {String} -- sample product url
        title {String} -- product title found on prod url
    """

    try:

        """Read company url text file and adds it to a set"""

        file1 = open(name+".txt", "r+")
        pattern = re.compile("^(http|https):\/\/")

        urls = set()
        for line in file1:
            line = file1.readline()
            line = line.strip()
            if not line:
                continue
            if pattern.match(line):
                holder = line
                urls.add(line)
                # print(line)
            # else :
            #     print(line)
        file1.close()

        """# Xpath extracting from produrl and title.Using sets to avoid duplicate"""

        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        page = requests.get(prodUrl, headers=headers)

        root = html.fromstring(page.text)
        tree = root.getroottree()
        title = "//*[. = '"+title+"']"
        result = root.xpath(title)
        refPath = set()
        for r in result:
            holder = tree.getpath(r)
            refPath.add(holder)
            # print(refPath)

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
                try:
                    flag = 0
                    prodUrls = set()
                    print("sleeping for 2 sec")
                    time.sleep(2)

                    pageHolder = requests.get(url, headers=headers)
                    treeHtml = html.fromstring(pageHolder.content)

                    """Checking xpath content in all urls, if content exist url is a produrl"""

                    for i in range(len(refPathFilter)):
                        xtitle = str(refPathFilter[i])+'/text()'
                        # print(xtitle)
                        element1 = treeHtml.xpath(xtitle)
                        # print(element1)
                        if len(element1) == 0:
                            if i == len(refPathFilter)-1:
                                flag += 1
                                break
                        else:
                            continue
                    """writing produrl to a txt file"""

                    if flag == 0:
                        row = str(url)
                        file1 = open(name+"ProdUrl.txt", "a")
                        file1.write(row + ",\n")
                        file1.close()
                    else:
                        print("no! : " + url)
                except:
                    print("broken link")

    except:
        print("txt file not found")
