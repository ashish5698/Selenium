import requests
from selenium import webdriver

browser = webdriver.Chrome("C:\\Users\Ravi\PycharmProjects\Sparks\chromedriver") #initializing chromedriver
browser.maximize_window() #maximizing the window
browser.get("https://brokenlinks.com")
links = browser.find_elements_by_xpath('.//a') #taking all links from website in a form of a list
check = 0
print("Below are the broken links")
for link in links:
    req = requests.head(link.get_attribute("href")) #get request header of each link for status code
    if(req.status_code>=400): # broken links are those with status code equal to or higher than 400
        check = 1
        print(link.get_attribute('href'), req.status_code)
if(check == 0):
    print("No broken links found")
