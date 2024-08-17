from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()

wait = WebDriverWait(driver, 30)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

normal_alert_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(1) > button"))
    )
normal_alert_button.click()

driver.switch_to.alert.accept()

confirmation_alert_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(2) > button"))
    )
confirmation_alert_button.click()

driver.switch_to.alert.dismiss()

prompt_alert_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(3) > button"))
    )
prompt_alert_button.click()

driver.switch_to.alert.send_keys("Test message")
driver.switch_to.alert.accept()

driver.quit()

