from selenium import webdriver
import random
import string

browser = webdriver.Chrome(executable_path="C:\\test\\ChromeDriver.exe")
browser.get('https://www.buyme.co.il/')

browser.find_element_by_id('ember617_chosen').click() # choose סכום
browser.find_element_by_xpath('//*[@id="ember617_chosen"]/div/ul/li[4]').click() # 199-299
browser.implicitly_wait(10)

browser.find_element_by_id('ember632_chosen').click() # choose אזור
browser.find_element_by_xpath('//*[@id="ember632_chosen"]/div/ul/li[3]').click() # מרכז

browser.find_element_by_id('ember641_chosen').click() # choose אזור
browser.find_element_by_xpath('//*[@id="ember641_chosen"]/div/ul/li[2]').click() # גיפט קארד מותגי אופנה

browser.find_element_by_class_name('btn-primary').click() # click on תמצא לי מתנה


