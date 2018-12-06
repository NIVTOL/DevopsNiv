import time
import random
import string

from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\test\\ChromeDriver.exe");
driver.get ("https://www.galabingo.com")

browser = webdriver.Chrome()
browser.get('https://www.galabingo.com/')
browser.find_element_by_class_name('trk-header-cta__join').click()

browser.find_element_by_class_name('fn-email-address').send_keys('test@playtech.com')
browser.find_element_by_id('username').send_keys("generateUserName"())
