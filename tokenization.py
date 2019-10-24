""" Import the necessary modules """
from bs4 import BeautifulSoup as bs
import bs4
from bs4.element import Tag
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import os, os.path, sys
import glob
from xml.etree import ElementTree

""" This function appends all annotated files """
def append_annotations(files):
    xml_files = glob.glob(files +"/*.xml")
    xml_element_tree = None
    new_data = ""
    for xml_file in xml_files:
        data = ElementTree.parse(xml_file).getroot()        
        temp = ElementTree.tostring(data, encoding='unicode')
        new_data += temp
    return(new_data)

""" This function removes special characters and punctuations """
def remov_punct(withpunct):
    punctuations = '''!()-[]{};:'"\,<>‘’®©™”|+./?@#$%^&*_~'''
    without_punct = ""
    char = 'nan'
    for char in withpunct:
        if char not in punctuations:
            without_punct = without_punct + char
    return(without_punct)

""" Append annotated xml files and create soup object """
files_path = "annotated_data"
allxmlfiles = append_annotations(files_path)
soup = bs(allxmlfiles, 'html5lib')

""" Define empty tags list """ 
tags = []

""" Define all stop words in the english language """
stop_words = set(stopwords.words('english'))

""" Tokenize annotated data and append tokens in tags list along with appropriate label """
""" Label 0 is assigned if token is not annotated """
""" Stopwords are removed regardless of whether tokens are annotated or not """
""" Punctuation is removed if tokens are not annotated """
for d in soup.find_all("document"):
   for wrd in d.contents:    
       NoneType = type(None)   
       if isinstance(wrd.name, NoneType) == True:
           withoutpunct = remov_punct(wrd)
           temp = word_tokenize(withoutpunct)
           for token in temp:
               if token not in stop_words:
                   tags.append((str(token),'0'))            
       else:
           temp = word_tokenize(wrd.text)
           for token in temp:
               if token not in stop_words:
                   tags.append((str(token).upper(),wrd.name))   
    
""" Write tokenized data along with labels to text file """
with open('tokenized_data.txt', 'w', encoding='utf-8-sig') as fp:
    fp.write('\n'.join('%s %s' % tag for tag in tags))
