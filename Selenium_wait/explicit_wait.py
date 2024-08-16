from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()

wait = WebDriverWait(driver, 30)

driver.get("https://tutorialsninja.com/demo/")

my_account = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".list-inline .dropdown .hidden-md"))
    )
my_account.click()

login_link = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Login"))
    )

login_link.click()