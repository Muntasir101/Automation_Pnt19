from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://www.google.com")

driver.get("http://bbc.com")

driver.quit()