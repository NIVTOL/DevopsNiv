from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\test\\ChromeDriver.exe");
driver.implicitly_wait(10)
driver.get ("https://translate.google.com")

print (driver.current_url)

print (driver.title)

# driver.find_element_by_id("gt-submit")
#
# my_list = driver.find_elements_by_class_name("jfk-button")
# my_list[1].click()   # 0 give me the sign in of google account
#
# driver.find_element_by_xpath("//*[@id='source']").send_keys("hello niv")
driver.find_element_by_id("source").send_keys("hello")
# driver.find_element_by_id("gt-submit").send_keys("niv") /clear
x = driver.find_element_by_id("gt-submit")
print(x.get_attribute("value"))
