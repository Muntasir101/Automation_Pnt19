from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.implicitly_wait(10)

driver.get("https://tutorialsninja.com/demo/")

desktops = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(1) > .dropdown-toggle"))
)

# mouse move to Desktops
# Create the object for Action Chains
actions = ActionChains(driver)
actions.move_to_element(desktops)
# perform the operation on the element
actions.perform()

mac = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.LINK_TEXT, "Mac (1)"))
)
mac.click()
