from bs4 import BeautifulSoup
import urllib.request
import csv 
import re
import os
# url = 'http://www.applebits.net/catalog/product_info.php?cPath=1_16&products_id=406'

# pageContent= request.get(url)

html = open("test3.html").read()

soup = BeautifulSoup(html, "lxml")
# image url extraction 
# image = soup.find('img', {'src' : re.compile(r'(jpe?g)|(png)$')})
# imageUrl = image['src']
# #Convert body content to string
# content = soup.find("body").get_text()
# content=content.strip()

soup =soup.prettify()

print(soup)
# tables = tables.replace(" ", "")

#Removing empty lines
# content = os.linesep.join([s for s in content.splitlines() if s])
# # if tables.match(r'^\s*$', line):
    
        
# print(content)
# print(tables[1])
# for tableBody in table:
#     tableBody = table.tbody
#     print(tableBody)

# table_rows = tableBody.find('tr')
# image = soup.find('img', {'src' : re.compile(r'(jpe?g)|(png)$')})
# imageUrl = image['src']
# print(table)
# for tr in table_rows:
#     td = tr.find_all('td')
    
#     row = [i.text for i in td]
#     # rowimage = [image.text for image in td]
#     print(row)
#     print(image)
#     print(imageUrl)

# print(soup.get_text())

# output_rows = []
# for table_row in table.findAll('tr'):
#     columns = table_row.findAll('td')
#     output_row = []
#     for column in columns:
#         output_row.append(column.text)
#     output_rows.append(output_row)

# with open('output.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(output_rows)