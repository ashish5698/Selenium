from selenium import webdriver
import os
import json
from urllib.request import *

# adding path to geckodriver to the OS environment variable
os.environ["PATH"] += os.pathsep + os.getcwd()
download_path = "photos/"

#taking input keywords
print("Enter which image to download: ")
searchtext = input()
num_requested = 10

if not os.path.exists(download_path + searchtext.replace(" ", "_")):
    os.makedirs(download_path + searchtext.replace(" ", "_"))

#setting up the google image search url and chromedriver
url = "https://www.google.co.in/search?q=" + searchtext + "&source=lnms&tbm=isch"
browser = webdriver.Chrome("C:\\Users\Ravi\PycharmProjects\Sparks\chromedriver")
browser.get(url)

#creating header and suitable extentions
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
extensions = {"jpg", "jpeg", "png", "gif"}
img_count = 0
downloaded_img_count = 1

#finding all the images present
imges = browser.find_elements_by_xpath('//div[contains(@class,"rg_meta")]')
print("Total images: {}\n".format(len(imges)))

#main code to test each image and download it in the preferred path
for img in imges:
    img_count += 1
    img_url = json.loads(img.get_attribute('innerHTML'))["ou"]
    img_type = json.loads(img.get_attribute('innerHTML'))["ity"]
    print("Downloading image {}:{}".format(img_count, img_url))
    try:
        if img_type not in extensions:
            img_type = "jpg"
        req = Request(img_url, headers=headers)
        raw_img = urlopen(req).read()
        f = open(download_path + searchtext.replace(" ", "_") + "/" + str(downloaded_img_count) + "." + img_type,
                 "wb")
        f.write(raw_img)
        f.close()
        downloaded_img_count += 1
    except Exception as e:
        print("Download failed: {}".format(e))
    finally:
        print()
    if downloaded_img_count >= num_requested+1:
        break

print("Total downloaded: {}/{}".format(downloaded_img_count-1, img_count))
