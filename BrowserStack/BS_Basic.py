

from selenium import webdriver

driver = webdriver.Remote(
    command_executor='https://<<user>>:<<access key>>@hub.browserstack.com:80/wd/hub')

driver.maximize_window()

driver.get("https://www.google.com")

if not "Google" in driver.title:
    raise Exception("Unable to load google page!")

print(driver.title)

driver.quit()
