#invoke libraries
from bs4 import BeautifulSoup as bs
import bs4
from bs4.element import Tag
import codecs
import nltk
from nltk import word_tokenize, pos_tag
from sklearn.model_selection import train_test_split
# import pycrfsuite
import os, os.path, sys
import glob
from xml.etree import ElementTree
import numpy as np
from sklearn.metrics import classification_report

# this function appends all annotated files
def append_annotations(files):
    xml_files = glob.glob(files +"/*.xml")
    xml_element_tree = None
    new_data = ""
    for xml_file in xml_files:
        data = ElementTree.parse(xml_file).getroot()
        #print ElementTree.tostring(data)        
        temp = ElementTree.tostring(data)
        new_data += str(temp)
    return(new_data)

# files_path = "sample"
handler = open('./sample/Reboot-IT1.xml', encoding = 'utf-8-sig').read()

# allxmlfiles = append_annotations(files_path)
soup = bs(handler, "html5lib")

tags = []

# Create a list of tokenized words with their respective labels
for d in soup.find_all("document"):
    for wrd in d.contents:
        NoneType = type(None)
        if isinstance(wrd.name, NoneType) == True:
            temp = word_tokenize(wrd)
            for token in temp:
                tags.append((token,0))
        else:
            temp = word_tokenize(str(wrd))
            for token in temp:
                tags.append((token,wrd.name))           
                
# Print out tokenized words along with their labels
for tag in tags:
    print(tag)