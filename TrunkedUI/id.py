import sys
import requests
import hashlib
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import unquote
import re
import xpathChk


def get_soup(link):
    """
    Return the BeautifulSoup object for input link
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    request_object = requests.get(link, headers=headers)
    soup = BeautifulSoup(request_object.content)
    return soup


def get_status_code(link):
    """
    Return the error code for any url
    param: link
    """
    try:
        error_code = requests.get(link).status_code
    except requests.exceptions.ConnectionError:
        return error_code


def find_internal_urls(def_url, urlchk, depth=0, max_depth=3):
    """
    Find URLs on page recursivly
    """
    all_urls_info = set()
    soup = get_soup(def_url)
    a_tags = soup.findAll("a", href=True)
    if depth > max_depth:
        return set()
    else:
        for a_tag in a_tags:
            if "http" not in a_tag["href"] and "/" in a_tag["href"]:
                url = urlchk + a_tag['href']
            elif "http" in a_tag["href"]:
                url = a_tag["href"]
            else:
                continue
            # print(url)
            if (((urlchk.replace("/", "")).replace(":", "")).replace("https", "")).replace("http", "") in url:
                all_urls_info.add(url)
    return all_urls_info


def flowStart(bname, burl, btitle, bdomain):
    urlSet = set()
    depth = 3
    all_page_urls = find_internal_urls(bdomain, bdomain, 3, 3)
    if depth > 1:
        for status_dict in all_page_urls:
            tempSet = find_internal_urls(status_dict, bdomain)
            for temUrl in tempSet:
                urlSet.add(temUrl)

    allurlfilename = "allurls"
    f = open(allurlfilename+".txt", "a")
    for val in urlSet:
        substr = unquote(val)
        if re.match('^http', val):
            f.write(val + "\n")
    f.close()
    xpathChk.xpath(allurlfilename, burl, btitle)
