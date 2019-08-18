# Import necessary modules
from html.parser import HTMLParser
from bs4 import BeautifulSoup, Comment
from urllib.request import urlopen as U
import requests
import html2text
import re
import imgkit
from PIL import Image
import pytesseract
from pytesseract import image_to_string
from selenium import webdriver
import os
os.environ["LANG"] = "en_US.UTF-8"

# Load html content of url and store it in the soup variable 
url = 'https://shop.workventures.com.au/product/lenovo-thinkpad-helix-2-in-1-laptop-tablet/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
response = requests.get(url, headers=headers)
content = response.content
soup = BeautifulSoup(content)

driver = webdriver.Chrome("C:/Users/sanch/Downloads/chromedriver_win32/chromedriver.exe")
driver.get(url)

font_sizes = []
elems = driver.find_elements_by_xpath("//*[contains(text(), '$')]")
for elem in elems:
    if elem.tag_name != 'script' or elem.tag_name != 'style':
        font_sizes.append(elem.value_of_css_property('font-size'))

fonts = []
for font in font_sizes:
    fonts.append(font.replace('px',''))

font_digits = []
for size in fonts:
    font_digits.append(float(size))

max_font = max(font_digits) 
max_font = int(max_font)
max_font = str(max_font)

for elem in elems:
    if elem.tag_name != 'script' or elem.tag_name != 'style':
        if max_font not in elem.value_of_css_property('font-size'):
            print('Not Max')
        else:
            print('Max')

# Remove all hidden elements from html content 
# for hidden in soup.body.find_all(style=re.compile(r'display:\s*none')):
#     hidden.decompose()

# for headless in (li for li in soup.find_all('li') if li.find('a')):
#     headless.decompose()

# tags = ['li', 'ul', 'ol']
# for tag in tags: 
#     for match in soup.findAll(tag):
#         match.replaceWithChildren()

# for label in soup.find_all('label'):
#     if label.find_next_siblings('input'):
#         label.decompose()

# for label in soup.find_all('label'):
#     if label.find_next_siblings('textarea'):
#         label.decompose()

# Remove elements which generate noise in web page
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

# [x.decompose() for x in soup.find_all('style')]

# for div in soup.find_all("div", {'class':'footer'}): 
#     div.decompose()

# for div in soup.find_all("div", {'class':'header'}): 
#     div.decompose()

# comments = soup.findAll(text=lambda text: isinstance(text, Comment))
# [comment.extract() for comment in comments]

# for tags in soup.findAll():
#         inner_text = tags.text
#         content = inner_text.strip()
#         if len(content) <= 3:
#             tags.extract()

# for tags in soup.findAll():
#         inner_text = tags.text
#         content = inner_text.strip()
#         if re.match(r'[©®™]', content):
#             tags.extract()

# for tags in soup.findAll():
#         inner_text = tags.text
#         content = inner_text.strip()
#         if re.match(r'[Copyright © ]', content):
#             tags.extract()

# flag = True
# while(flag):
#     count = 0
#     for tags in soup.findAll():
#         inner_text = tags.text
#         content = inner_text.strip()
#         if len(content) == 0:
#             count = count+1
#             tags.extract()
#     if(count > 0):
#         flag = True
#     else:
#         flag = False


            
# with open('test.html', 'w', encoding='utf-8-sig') as f:
#     f.write(str(soup))

# imgkit.from_file('test.html', 'test.png')

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# img = Image.open("test.png")
# text = image_to_string(img)     

# # Specify file name
# filename = "test.txt"

# # Write text to file
# with open(filename, 'w') as f:
#     f.write(text)

# # Read file and store contents in set while preserving order 
# content = open(filename, 'r')
# lines = content.readlines()
# texts = sorted(set(lines), key=lines.index)

# # Remove strings whose length is less than or equal to 3 from set
# for strings in texts:
#     if len(strings) <= 3:
#         texts.remove(strings)

# # Remove lines which contain only special characters and contain copyright symbol
# # Write filtered out text to file  
# with open(filename, 'w') as fil:
#     for line in texts:
#         if not re.match(r'^[_\W]+$', line):
#             if not re.match(r'[©®™]', line):
#                 if not re.match(r'[Copyright © ]', line):
#                     fil.write(line)

