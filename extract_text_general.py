""" Import necessary modules """
from html.parser import HTMLParser
from bs4 import BeautifulSoup, Comment
from urllib.request import urlopen as U
import requests
import re
import os
import time

def extract_text_general():
    
    file_name = "extractedtext_"

    file_num = 1

    product_urls = []

    """ Reading lines from product text file """
    file_lines = []
    with open("producturl.txt", "r") as fs:
        for line in fs:
            currentLine = line.rstrip().split(',')
            file_lines.append(currentLine)

    """ Extracting and storing product urls """
    urls = []
    for fl in file_lines:
        urls.append(fl[0])

    """ Converting product urls list to set """
    urls = sorted(set(urls), key=urls.index)

    """ Loop through all product urls """
    for url in urls:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

        try:
            """ Load html content of url and store it in the soup variable """
            response = requests.get(url, headers=headers, allow_redirects=False)
            content = response.content
            soup = BeautifulSoup(content)

            """ Remove all hidden elements from html """
            for hidden in soup.body.find_all(style=re.compile(r'display:\s*none')):
                hidden.decompose()

            """ Remove all list elements containing anchor elements from html """
            for headless in (li for li in soup.find_all('li') if li.find('a')):
                headless.decompose()

            """ Replace all li, ul, ol elements with their children elements in html """
            tags = ['li', 'ul', 'ol']
            for tag in tags:
                for match in soup.findAll(tag):
                    match.replaceWithChildren()

            """ Remove all label elements whose next sibling is input element from html """
            for label in soup.find_all('label'):
                if label.find_next_siblings('input'):
                    label.decompose()

            """ Remove all label elements whose next sibling is textarea element from html """
            for label in soup.find_all('label'):
                if label.find_next_siblings('textarea'):
                    label.decompose()

            """ Remove elements which generate noise in web page from html """
            [x.decompose() for x in soup.find_all('script')]
            [x.decompose() for x in soup.find_all('head')]
            [x.decompose() for x in soup.find_all('title')]
            [x.decompose() for x in soup.find_all('meta')]
            [x.decompose() for x in soup.find_all('noscript')]
            [x.decompose() for x in soup.find_all('select')]
            [x.decompose() for x in soup.find_all('img')]
            [x.decompose() for x in soup.find_all('textarea')]
            [x.decompose() for x in soup.find_all('input')]
            [x.decompose() for x in soup.find_all('button')]
            [x.decompose() for x in soup.find_all('nav')]
            [x.decompose() for x in soup.find_all('a')]
            [x.decompose() for x in soup.find_all('footer')]
            [x.decompose() for x in soup.find_all('iframe')]
            [x.decompose() for x in soup.find_all('svg')]
            [x.decompose() for x in soup.find_all('aside')]
            [x.decompose() for x in soup.find_all('header')]
            [x.decompose() for x in soup.find_all('style')]

            """ Remove all div elements which have footer class from html """
            for div in soup.find_all("div", {'class':'footer'}):
                div.decompose()

            """ Remove all div elements which have header class from html """
            for div in soup.find_all("div", {'class':'header'}):
                div.decompose()

            """ Remove all comments """
            comments = soup.findAll(text=lambda text: isinstance(text, Comment))
            [comment.extract() for comment in comments]

            """ Remove all elements with content containing copyright symbol from html """
            for tags in soup.findAll():
                inner_text = tags.text
                content = inner_text.strip()
                if re.match(r'[©®™]', content):
                    tags.extract()

            for tags in soup.findAll():
                inner_text = tags.text
                content = inner_text.strip()
                if re.match(r'[Copyright © ]', content):
                    tags.extract()

            """ Remove all empty elements from html until no empty elements are left """
            flag = True
            while(flag):
                count = 0
                for tags in soup.findAll():
                    inner_text = tags.text
                    content = inner_text.strip()
                    if len(content) == 0:
                        count = count+1
                        tags.extract()
                if(count > 0):
                    flag = True
                else:
                    flag = False

            """ Setting path to directory containing text files """
            #cur_path = os.path.dirname(__file__)
            #text_path = os.path.relpath(file_name+str(file_num)+'.txt', cur_path)

            """ Extract text from soup object """
            text = soup.get_text().upper()

            """ Write text to file """
            with open("./extracted_data/" + file_name+str(file_num)+'.txt', 'w', encoding ='utf-8-sig') as f:
                f.write(text)

            """ Read file and store contents in set while preserving order """
            content = open("./extracted_data/" + file_name+str(file_num)+'.txt', 'r', encoding='utf-8-sig')
            lines = content.readlines()
            texts = sorted(set(lines), key=lines.index)

            """ Remove strings whose length is less than or equal to 3 from set """
            for strings in texts:
                if len(strings) <= 3:
                    texts.remove(strings)

            """ Remove lines which contain only special characters and contain copyright symbol """
            """ Write filtered out text to file """  
            with open("./extracted_data/" + file_name+str(file_num)+'.txt', 'w', encoding ='utf-8-sig') as fil:
                for line in texts:
                    if not re.match(r'^[_\W]+$', line):
                        if not re.match(r'[©®™]', line):
                            if not re.match(r'[Copyright © ]', line):
                                fil.write(line)

            """ Store working product urls in product_urls list """
            product_urls.append(url)

            file_num = file_num + 1

        except requests.exceptions.ConnectionError:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            continue

        except(AttributeError) as e:
            pass

    """ Write working product urls to a text file """
    count = 0
    with open('working_product_urls.txt', 'w') as fp:
        for url in product_urls:
            count = count + 1
            if(count != len(product_urls)):
                fp.write(url+",\n")
            else:
                fp.write(url)