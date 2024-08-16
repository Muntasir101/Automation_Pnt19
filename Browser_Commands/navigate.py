import time

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.google.com")
time.sleep(5)

driver.get("https://bbc.com")
time.sleep(5)

driver.back()  # back to google
time.sleep(2)

driver.forward()  # forward to bbc

driver.refresh()

driver.quit()
