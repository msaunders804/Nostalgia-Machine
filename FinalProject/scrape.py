# Nostalgia Machine: image downloading script

# Adapted from:
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

import lxml
import requests
import urllib
import urllib3
from urllib3.exceptions import InsecureRequestWarning

import datetime
import time


urllib3.disable_warnings(InsecureRequestWarning)

folder_name = 'testpictures'
max_count = 10       #number of pictures you want to download - eventually, change to ~1000

#Create an empty folder in which to store pictures once they download
if not os.path.exists(folder_name):
    os.mkdir(folder_name)


def download_google_images(search_term):

    # Initialize driver to open a Firefox browser
    # Note: if anyone else wants to dry this for themselves, you'll need to download the correct geckodriver.exe for
        # your machine and then change the executable_path name below to the location of that .exe file
    driver = webdriver.Firefox(executable_path="C:/Users/olivi_000/Desktop/vboxshared/pyth/geckodriver.exe")
    # Concatenate the search_term onto the end of google's image search page to get url
    search_url = 'https://www.google.com/search?q=' # + search_term
    # Navigates browser to page specified by search_url - in this case, the home page for Google Images
    driver.get(search_url)
    # Locates the search bar and types in the search keywords
    driver.find_element_by_name("q").send_keys(search_term + Keys.ENTER)

    # Navigate to body of page - otherwise, program will try to save google logo too
    page_body = driver.find_element_by_tag_name('body')

    # Use html tags to locate search images on the page - store in array (?)
    #images = driver.find_elements_by_tag_name('img')
    #for im in images:
        # Print url for each image
        #print(im.get_attribute('src'))

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')
    images = soup.find_all('img')

    url_list = []   # initialize empty list for storing urls of the images
    for im in images:
        try:
            url = im['data-src']     # some images have this attribute, but some might not
            if not url.find('https://'):    # if substring 'https://' is not found in url
                url_list.append(url)
        except:
            try:
                url = im['src']   # if 'data-src' attribute isn't found, this is a possible alternative
                if not url.find('https://'):
                    url_list.append(im['src'])
            except:
                print('No found source for this image :(')

    # Count tracks the number of successfully download images thus far
    count = 0
    # Iterate through the parsed-out urls
    for url in url_list:
        try:
            res = requests.get(url, verify=False, stream=True)
            rawdata = res.raw.read()
            # open the testpictures folder and give the photo a numbered label
            with open(os.path.join(folder_name, 'img_' + str(count) + '.jpg'), 'wb') as f:
                # Store rawdata in the folder of pictures
                f.write(rawdata)
                count += 1
        except Exception as e:
            print('Failed to write rawdata.')
            print(e)

    time.sleep(5)
    # driver.close()    #Close the browser

if __name__ == "__main__":
    tvDict = {}  # dictionary of search terms- stores    integer: Name of TV show
    tvDict[0] = 'Spongebob screencaps'
    tvDict[1] = 'Fairly Oddparents screencaps'
    tvDict[2] = 'Danny Phantom screencaps'
    tvDict[3] = 'Rocket Power screencaps'

    search_term = tvDict[0]
    download_google_images(search_term)
