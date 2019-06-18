from selenium import webdriver
import time

browser = webdriver.Chrome("C:\\Users\Ravi\PycharmProjects\Sparks\chromedriver") #loading the chrome webdriver
browser.maximize_window()

browser.get("https://www.google.com/gmail/") #loading the website
time.sleep(1)

#finding out the box to enter email id and enter the id
email_name = browser.find_element_by_id("identifierId")
email_name.clear()
email_name.send_keys("ashishkamatala@gmail.com")
email_button = browser.find_element_by_id("identifierNext")
email_button.click()
time.sleep(1)

#finding password box and entering password
email_password = browser.find_element_by_name("password")
email_password.clear()
email_password.send_keys("saibaba5698")
email_password_button = browser.find_element_by_id("passwordNext")
email_password_button.click()
time.sleep(10)

#finding the compose option and clicking it
email_compose = browser.find_element_by_css_selector(".aic .z0 div")
email_compose.click()
time.sleep(1)

#finding the 'to' option and entering the email id
send_mail = browser.find_element_by_css_selector(".oj div textarea")
send_mail.send_keys("kamatalaashish@gmail.com")
#time.sleep(1)

#finding subject box and entering the subject
subject = browser.find_element_by_name("subjectbox")
subject.send_keys("hello world")
#time.sleep(1)

#finding the main body and writing the message
mainMssg = browser.find_element_by_css_selector("div[aria-label='Message Body']")
mainMssg.send_keys("have a great day")

#finding the send button and clicking it
sendElem = browser.find_element_by_xpath("//div[text()='Send']")
sendElem.click()

