# Google image web scraper for Nostalgia Machine project
# Adapted from:
#     https://github.com/hardikvasa/google-images-download/issues/301#issuecomment-587097949
#     and
#     https://towardsdatascience.com/image-scraping-with-python-a96feda8af2d
#
###############################################################################################################

# todo - fix bug that saves empty image files
# todo - fix scrolling issue at beginning of program

import time
import shutil
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import os
import urllib3
from urllib3.exceptions import InsecureRequestWarning


if __name__ == '__main__':

    urllib3.disable_warnings(InsecureRequestWarning)
    t0 = time.time()    # Start program timer!

    folder_name = 'testpictures'    # Destination folder in which to save images
    search_keywords = "Spongebob screencaps"
    max_images = 1000

    # Create an empty folder in which to store pictures once they download
    if not os.path.exists(folder_name):  # If folder doesn't exist, just make a new one
        os.mkdir(folder_name)
    else:  # If folder already exists, empty its contents, delete the folder, then make a new one
        shutil.rmtree(folder_name)
        os.rmdir(folder_name)
        os.mkdir(folder_name)

    # Use webdriver, open an empty Firefox browser
    driver = webdriver.Firefox(executable_path="C:/Users/olivi_000/Desktop/vboxshared/pyth/geckodriver.exe")
    # Navigate browser to page specified by search_url - in this case, the home page for Google Images
    search_url = 'https://www.google.com/imghp?hl=en'
    driver.get(search_url)
    # Locate the search bar and types in the search keywords
    driver.find_element_by_name("q").send_keys(search_keywords + Keys.ENTER)
    # Give the page some time to load the search results - if you don't, the next part won't work!
    time.sleep(3)

    url_set = set()  # Initialize empty set for storing urls - allows you to ignore any duplicates
    url_count = 0     # Size of url_set
    results_start = 0  # This marks the location of the page where the current range of search results begins

    # Keep going until you've reached the desired number of images
    while url_count < max_images:

        # This line of code uses a JavascriptExecutor (an interface of the selenium webdriver) which scrolls all the way
        # to the bottom of the current results. Doing this **may** automatically load more search results as well.
        print("Scrolling down ...")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Get all image thumbnails (i.e. the long list of results which your search initially displays, before any clicking)
        thumb_results = driver.find_elements_by_css_selector("img.Q4LuWd")
        number_results = len(thumb_results)  # TOTAL number of thumbnail results loaded so far

        # This condition will be met if you reach the end of the search results
        if number_results == results_start:
            print("Reached end of results. Collected {} image links!".format(url_count))
            break

        print(f"Found {number_results} total search results. Extracting links from range {results_start}-{number_results}")

        # Loops through a fixed range of urls - this is usually fewer than the total number of search results currently loaded
        for thumb_img in thumb_results[results_start:number_results]:
            # Attempt to click every thumbnail such that we can get the real image behind it
            try:
                thumb_img.click()
                time.sleep(0.1)
            except Exception:  # if any exception occurs, just skip the current image and move on to the next one
                continue

            # Now that you've clicked on the image, extract the image url
            actual_images = driver.find_elements_by_css_selector('img.n3VNCb')
            for actual_image in actual_images:
                # Make sure that 'src' is a url containing the substring 'http'
                if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                    # Add new url to the set
                    url_set.add(actual_image.get_attribute('src'))

            url_count = len(url_set)  # Update the size of the image_url set

            # Break out of loop if you've collected the desired number of urls, or when you run out of search results
            if url_count >= max_images or results_start == number_results:
                print("Done! Collected {} image links!".format(url_count))
                break   # End the while loop
            elif results_start == number_results:
                print("Reached end of results. Collected {} image links!".format(url_count))
                break
        else:
            print("Found", url_count, "total image links, looking for more ...")
            time.sleep(3)
            # Although scrolling to the bottom of the page will automatically load more results for your first few attempts,
            # eventually this will stop and you'll have to click a "show more results" button before continuing
            show_more_button = driver.find_element_by_css_selector(".mye4qd")
            if show_more_button:  # If this button exists...
                print("Pressing the 'show more results' button ...")
                driver.execute_script("document.querySelector('.mye4qd').click();")     # ... click it.

        # Move the result starting point further down
        results_start = len(thumb_results)

    driver.close()

    # At this point, we've gathered all the urls we need and the web browser window is closed. Now we need to save those
    # images into a local folder.
    print("Attempting to save images to {} ...".format(folder_name))

    # Use count to track the number of successfully DOWNLOADED images thus far
    download_count = 0
    # Iterate through the set of urls
    for url in url_set:
        try:
            # Use an HTTP get request to read the actual image data from the url
            response = requests.get(url, verify=False, stream=True)     # doesn't need to verify host's SSL certificate; don't download body of response immediately
            raw_data = response.raw.read()
            # The os.path.join() method concatenates the paths of folder_name and the new image file
            # e.g. f = ....PycharmProjects/webscraping/testpictures/img_1.jpg
            with open(os.path.join(folder_name, 'img_' + str(download_count) + '.jpg'), 'wb') as f:
                f.write(raw_data)
                download_count += 1
        except Exception as e:
            print('Failed to write rawdata.')

    t1 = time.time()
    print("Program took {} seconds to save {} images".format(t1-t0, download_count))