from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\test\\ChromeDriver.exe");

driver.get ("http://www.ebay.com")

print (driver.current_url)

print (driver.title)

#print (driver.page_source)

# driver.quit();   close the browser

# driver.refresh()  #[ /forward/back) ()

driver.find_element_by_link_text()

