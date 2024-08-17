from Screenshot import Screenshot
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
url = "https://www.google.com/"
driver.get(url)

element = driver.find_element(By.CSS_SELECTOR, "img[alt='Google']")


driver.quit()