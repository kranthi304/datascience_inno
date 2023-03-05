import streamlit as st
from matplotlib import image
import os

# st.title("Dashboard - Titanic Data")

# # absolute path to this file
# FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# # absolute path to this file's root directory
# PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# # absolute path of directory_of_interest
# dir_of_interest = os.path.join(PARENT_DIR, "resources")

# IMAGE_PATH = os.path.join(dir_of_interest, "images", "titanic.jpg")
# DATA_PATH = os.path.join(dir_of_interest, "data", "titanic.csv")

# img = image.imread(IMAGE_PATH)
# st.image(img)

st.title("Dashboard -Dalal Street news")

# # absolute path to this file
#FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# # absolute path to this file's root directory
# PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# # absolute path of directory_of_interest
# dir_of_interest = os.path.join(PARENT_DIR, "resources")

# IMAGE_PATH = os.path.join(dir_of_interest, "images", "titanic.jpg")
# DATA_PATH = os.path.join(dir_of_interest, "data", "titanic.csv")

# img = image.imread(IMAGE_PATH)
# st.image(img)

from bs4 import BeautifulSoup
import time
import sys
import requests

try:
    page=requests.get('https://www.moneycontrol.com/')
except Exception as e:
    error_type,error_obj,error_info=sys.exc_info()
    print('Error for link',url)
    print(error_type,'Line:',error_info.tb_lineno)

time.sleep(2)
soup=BeautifulSoup(page.text,'html.parser')
links=soup.find_all('div',attrs={'class':'clearfix ltsnewsbx'})

for i in links:
    print(i.text)
    print('\n')
