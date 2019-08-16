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


# Load html content of url and store it in the soup variable 
url = 'https://www.amtelectronics.net.au/product/apple-ipad-128gb-wi-fi-gold-6th-gen/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
response = requests.get(url, headers=headers)
content = response.content
soup = BeautifulSoup(content)

# Remove all hidden elements from html content 
for hidden in soup.body.find_all(style=re.compile(r'display:\s*none')):
    hidden.decompose()

# Remove elements which generate noise in web page
[x.extract() for x in soup.find_all('script')]
[x.extract() for x in soup.find_all('style')]
[x.extract() for x in soup.find_all('head')]
[x.extract() for x in soup.find_all('title')]
[x.extract() for x in soup.find_all('meta')]
[x.extract() for x in soup.find_all('noscript')]
[x.extract() for x in soup.find_all('select')]
[x.extract() for x in soup.find_all('img')]
[x.extract() for x in soup.find_all('textarea')]
[x.extract() for x in soup.find_all('input')]
[x.extract() for x in soup.find_all('button')]
[x.extract() for x in soup.find_all('nav')]
[x.extract() for x in soup.find_all('a')]
[x.extract() for x in soup.find_all('footer')]
[x.extract() for x in soup.find_all('iframe')]

for div in soup.find_all("div", {'class':'footer'}): 
    div.extract()

for div in soup.find_all("div", {'class':'header'}): 
    div.extract()

comments = soup.findAll(text=lambda text: isinstance(text, Comment))
[comment.extract() for comment in comments]

for div in  soup.findAll("div", {"aria-hidden" : "true"}):
    div.extract()

with open('test.html', 'w') as f:
    f.write(str(soup))

imgkit.from_file('test.html', 'test.png')

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = Image.open("test.png")
text = image_to_string(img)

# Specify file name
filename = "test.txt"

with open(filename, 'w') as f:
    f.write(text)

# Write text to file

#Read file and store contents in set while preserving order 
# content = open(filename, 'r', encoding="utf-8")
# lines = content.readlines()
# texts = sorted(set(lines), key=lines.index)

# Remove strings whose length is less than or equal to 3 from set
# for strings in texts:
#     if len(strings) <= 3:
#         texts.remove(strings)

# Remove lines which contain only special characters and contain copyright symbol
# Write filtered out text to file  
# with open(filename, 'w', encoding="utf-8") as fil:
#     for line in texts:
#         if not re.match(r'^[_\W]+$', line):
#             if not re.match(r'[©®™]', line):
#                 if not re.match(r'[Copyright © ]', line):
#                     fil.write(line)
