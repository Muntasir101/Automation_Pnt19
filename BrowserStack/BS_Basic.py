"""
Browser stack :
email: cisicey819@ndiety.com
pass: cisicey819@ndiety.com

browserstack-sdk python .\Project1-Fight_cost\bs.py
"""

from selenium import webdriver

driver = webdriver.Remote(
    command_executor='https://muntasir_zx5P0S:HswQH1tWVxrfWVeFCaye@hub.browserstack.com:80/wd/hub')

driver.maximize_window()

driver.get("https://www.google.com")

if not "Google" in driver.title:
    raise Exception("Unable to load google page!")

print(driver.title)

driver.quit()
