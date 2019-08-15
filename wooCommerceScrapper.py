from html.parser import HTMLParser
from bs4 import BeautifulSoup, Comment
from urllib.request import urlopen as U
import requests
import html2text
import re


url = 'https://www.amtelectronics.net.au/product/team-lightning-cable/'
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')

[x.extract() for x in soup.find_all('script')]
[x.extract() for x in soup.find_all('style')]
[x.extract() for x in soup.find_all('head')]
[x.extract() for x in soup.find_all('title')]
[x.extract() for x in soup.find_all('meta')]
[x.extract() for x in soup.find_all('noscript')]
[x.extract() for x in soup.find_all('select')]
[x.extract() for x in soup.find_all('img')]
[x.extract() for x in soup.find_all('textarea')]
[x.extract() for x in soup.find_all('nav')]
[x.extract() for x in soup.find_all('button')]
comments = soup.findAll(text=lambda text:isinstance(text, Comment))
[comment.extract() for comment in comments]

for hidden in soup.body.find_all(style=re.compile(r'display:\s*none')):
    hidden.decompose()

soup.find('div', id="tab-reviews").decompose()

for div in soup.find_all("div", {'class':'header'}): 
    div.decompose()

for div in soup.find_all("div", {'class':'footer'}): 
    div.decompose()

for atag in soup.find_all('a'):
    atag.extract()

for textbox in soup.find_all('input'):
    textbox.extract()

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

with open('prod1.txt', 'w') as f:
    f.write(text)

content = open('prod1.txt', 'r')
lines = content.readlines()
texts = sorted(set(lines), key=lines.index)

for strings in texts:
    if len(strings) <= 3:
        texts.remove(strings)

with open('prod1.txt', 'w') as fil:
    for line in texts:
        if not re.match(r'^[_\W]+$', line) and not re.match(r'[©®™]', line):
            fil.write(line) 