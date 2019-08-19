#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.amtelectronics.net.au/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c = r.content

soup = BeautifulSoup(c,"html.parser")

#print(soup.prettify())

all = soup.find_all("ul", {"class":"cat-ul"})

#all[0].find("ul",{"class":"cat-ul"}).text

#all[0].find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")


# In[2]:


all = soup.find_all("ul", {"class":"cat-ul"})


# In[ ]:


all


# In[3]:


data = all[0].find_all('li')


# In[6]:


len(data)


# In[5]:


l={}
for li in data:
    l['links'] = li.find('a')['href']
    #print(li.find('a')['href'])
    print(li.find('a').contents[0])


# In[ ]:


type(data)


# In[ ]:


# for li in soup.findAll('ul', attrs={'class':'cat-ul'}):
#     print(li.find_all('a')['href'])
#     print(li.find_all('a').contents)

# links=soup.findAll('a')
# for link in links:
#     print(link['href'])
#     print(link.contents)


# In[ ]:


for item in all:
    print(item.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")) #.find will only grab first occurance of the matched class .finall will grab everything
    print(item.find_all("span",{"class":"propAddressCollapse"})[0].text)
    print(item.find_all("span",{"class":"propAddressCollapse"})[1].text)
    try:
        print(item.find("span",{"class":"infoBed"}).find("b").text)
    except:
        print(None)
    
    try:
        print(item.find("span",{"class":"infoSqFt"}).find("b").text)
    except:
        print(None)
    
    try:
        print(item.find("span",{"class":"infoValueFullBath"}).find("b").text)
    except:
        print(None)
    
    try:
        print(item.find("span",{"class":"infoValueHalfBath"}).find("b").text)
    except:
        print(None)
    for column_group in item.find_all("div",{"class":"columnGroup"}):
        for feature_group, feature_name in zip(column_group.find_all("span",{"class":"featureGroup"}),column_group.find_all("span",{"class":"featureName"})):
            #print(feature_group.text, feature_name.text)
            if "Lot Size" in feature_group.text:
                print(feature_name.text)
    print(" ")


# In[ ]:


l = []
base_url = "https://www.amtelectronics.net.au/"
for page in range(0,30,10):
    #print(base_url+str(page)+".html")
    r=requests.get(base_url+str(page)+".html", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    all = soup.find_all("div", {"class":"propertyRow"})
    #print(soup.prettify())
    for item in all:
        d = {}
        d["Locality"] = item.find_all("span",{"class":"propAddressCollapse"})[0].text
        d["Address"] =  item.find_all("span",{"class":"propAddressCollapse"})[1].text
        d["Price"] = item.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","") #.find will only grab first occurance of the matched class .finall will grab everything

        try:
            d["Beds"] = item.find("span",{"class":"infoBed"}).find("b").text
        except:
            d["Beds"] = None

        try:
            d["Area"] = item.find("span",{"class":"infoSqFt"}).find("b").text
        except:
            d["Area"] = None

        try:
            d["Full Baths"] = item.find("span",{"class":"infoValueFullBath"}).find("b").text
        except:
            d["Full Baths"] = None

        try:
            d["Half Baths"] = item.find("span",{"class":"infoValueHalfBath"}).find("b").text
        except:
            d["Half Baths"] = None
        for column_group in item.find_all("div",{"class":"columnGroup"}):
            for feature_group, feature_name in zip(column_group.find_all("span",{"class":"featureGroup"}),column_group.find_all("span",{"class":"featureName"})):
                #print(feature_group.text, feature_name.text)
                if "Lot Size" in feature_group.text:
                    d["Lot Size"] = feature_name.text
                    #print(" ")
        l.append(d)


# In[ ]:


len(l)


# In[ ]:


import pandas as pd
df = pd.DataFrame(l)


# In[ ]:


df


# In[ ]:


df.to_csv("Output.csv")


# In[ ]:


pwd


# In[ ]:




