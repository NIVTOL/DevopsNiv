from selenium import webdriver

browser = webdriver.Chrome(executable_path="C:\\test\\ChromeDriver.exe")
browser.get('https://www.buyme.co.il/')

selenium.click("xpath=(.//*[normalize-space(text()) and normalize-space(.)='ושולחים בהפתעה ישר לנייד או למייל'])[1]/following::span[2]")
selenium.click("xpath=(.//*[normalize-space(text()) and normalize-space(.)=concat('100-199 ש', '\"', 'ח')])[1]/following::li[1]")
