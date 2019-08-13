# Import necessary modules
from html.parser import HTMLParser
from bs4 import BeautifulSoup, Comment
from urllib.request import urlopen as U
import requests
import html2text
import re

# Load html content of url and store it in the soup variable 
url = 'http://www.applebits.net/catalog/product_info.php?products_id=933'
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
comments = soup.findAll(text=lambda text: isinstance(text, Comment))
[comment.extract() for comment in comments]

# Convert remaining html content to text
text = soup.get_text()

# Break text into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())

# Break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

# Remove all blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

# Specify file name
filename = "Book1.txt"

# Write text to file
with open(filename, 'w', encoding="utf-8") as f:
    f.write(text)

# Read file and store contents in set while preserving order 
content = open(filename, 'r', encoding="utf-8")
lines = content.readlines()
texts = sorted(set(lines), key=lines.index)

# Remove strings whose length is less than or equal to 3 from set
for strings in texts:
    if len(strings) <= 3:
        texts.remove(strings)

# Remove lines which contain only special characters and contain copyright symbol
# Write filtered out text to file  
with open(filename, 'w', encoding="utf-8") as fil:
    for line in texts:
        if not re.match(r'^[_\W]+$', line):
            if not re.match(r'[©®™]', line):
                if not re.match(r'[Copyright © ]', line):
                    fil.write(line)
