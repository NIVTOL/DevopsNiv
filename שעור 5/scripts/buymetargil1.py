from selenium import webdriver
import random
import string



browser = webdriver.Chrome(executable_path="C:\\test\\ChromeDriver.exe")
browser.get('https://www.buyme.co.il/')
browser.find_element_by_class_name('no-underline').click()
browser.find_element_by_class_name('header-link').click()


# browser.find_element_by_class_name('fn-email-address').send_keys('test@playtech.com')
browser.find_element_by_id('ember901').send_keys("niv")
browser.find_element_by_id('ember902').send_keys("nivtol@gmail.com")
browser.find_element_by_id('valPass').send_keys("London10")
browser.find_element_by_id('ember904').send_keys("London10")

browser.find_element_by_xpath('//*[@id="ember900"]/div[5]/div/label').click()
browser.find_element_by_xpath ('//*[@id="ember900"]/button').click()
