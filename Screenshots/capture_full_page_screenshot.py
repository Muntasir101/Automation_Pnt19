import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()

wait = WebDriverWait(driver, 30)

driver.get("https://apple.com")

# scroll down
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(2)

page_height = driver.execute_script("return document.body.scrollHeight")
driver.set_window_size(1920, page_height)

driver.save_screenshot("apple.png")

driver.quit()
