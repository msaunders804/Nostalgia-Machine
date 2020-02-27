#Nostalgia Machine: image downloading script

#Adapted from:
#     https://github.com/hardikvasa/google-images-download/issues/301#issuecomment-587097949
#     and
#     https://towardsdatascience.com/image-scraping-with-python-a96feda8af2d

from selenium import webdriver
import requests

from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

import json
import os
import argparse

import requests
import urllib
import urllib3
from urllib3.exceptions import InsecureRequestWarning

import datetime
import time

urllib3.disable_warnings(InsecureRequestWarning)

searchterm = 'Spongebob screencaps'
searchurl = 'https://www.google.com/search?q=' + searchterm
dirs = 'testpictures'
maxcount = 10       #number of pictures you want to download

#Create an empty folder in which to store pictures once they download
if not os.path.exists(dirs):
    os.mkdir(dirs)

def download_google_images():

    #Initialize driver to open a Firefox browser
    #Note: if anyone else wants to dry this for themselves, you'll need to download the correct geckodriver.exe for
        #  your machine and then change the executable_path name below to the location of that .exe file
    driver = webdriver.Firefox(executable_path="C:/Users/olivi_000/Desktop/vboxshared/pyth/geckodriver.exe")

    #Navigates browser to page specified by searchurl
    driver.get(searchurl)

    #Locates the search bar and types in the search keywords - don't need this anymore, may delete later
    #driver.find_element_by_name("q").send_keys(searchterm + Keys.ENTER)

    #Use html tags to locate the images on the page - store in array (?)
    images = driver.find_elements_by_tag_name('img')
    for im in images:
        #Print url for each image
        print(im.get_attribute('src'))

    driver.close()    #Close the browser

if __name__ == "__main__":
    download_google_images()
