from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()

wait = WebDriverWait(driver, 30)

driver.get("https://tutorialsninja.com/demo/index.php?route=product/product&product_id=42")

color = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "select[name='option[217]']"))
    )


color_options = Select(color)
color_options.select_by_value("1")

