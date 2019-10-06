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
import extract_text_general
import store_productURL
from googleapiclient import discovery, http
from oauth2client.client import GoogleCredentials
from google.cloud import storage

credentials = GoogleCredentials.get_application_default()

service = discovery.build('storage', 'v1', credentials=credentials)


def xpath(name, prodUrl, title, bname):
    """Read url from txt and filters out Product Urls only
    Arguments:
        name {String} -- file name
        prodUrl {String} -- sample product url
        title {String} -- product title found on prod url
    """
    #try:
    
    client = storage.Client()

    bucket_name = "trunkedfilestorage"

    bucket = client.get_bucket(bucket_name)
    
    
    """Read company url text file and adds it to a set"""
    blob = bucket.get_blob('allurls.txt')
    out_file = open("allurls.txt", 'wb')
    file_content = blob.download_as_string()
    out_file.write(file_content)
    out_file.close()
    
    file1 = open("allurls.txt", "r+")
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
                    element1 = treeHtml.xpath(xtitle)
                    if len(element1) == 0:
                        if i == len(refPathFilter)-1:
                            flag += 1
                            break
                    else:
                        continue
                """writing produrl to a txt file"""

                if flag == 0:
                    row = str(url)
                    file1 = open("producturl.txt", "a")
                    file1.write(row + ",\n")
                    file1.close()
      
                    
                else:
                    print("no! : " + url)
                
            except:
                print("broken link")
            
    filename = 'producturl.txt'
    bucket = 'trunkedfilestorage' 
    body = {'name': 'producturl.txt'}
    req = service.objects().insert(bucket=bucket, body=body, media_body=filename)    
    resp = req.execute()
                

    extract_text_general.extract_text_general()
    store_productURL.storeProdURL(bname)

    #except:
        #print("txt file not found")
