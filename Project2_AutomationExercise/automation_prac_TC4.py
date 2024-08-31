import time

import selenium.webdriver.support.select
from select import select
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement
from selenium.webdriver.support.ui import Select

from Automation.automation_prac_TC1 import account_creation

# initial info
name = "Ron Wisley"
email = "riyak8584333@avashost.com"
password = "121212"
company = "People and Tech"
address = "223/B, baker Street, East London"
address2 = "44/6, new york, USA"



# 1. Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

#creating new account everytime to avoid getting error of invalid email or password
account_creation()

# 2. Navigate to URL
driver.get('http://automationexercise.com')


# 3. Verify that home page is visible successfully
home_button_text = driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(1) > a").text
expected_home_button_text = "Home"

if home_button_text == expected_home_button_text:
    print("Home page is visible")
else:
    print("Home page is not visible")


# 4. click on the signup/login button
login_button = driver.find_element(By.XPATH,"/html//header[@id='header']/div[@class='header-middle']//ul[@class='nav navbar-nav']//a[@href='/login']")
login_button.click()


# 5. Verify 'Login to your account' is visible
Login_to_your_account = driver.find_element(By.CSS_SELECTOR, ".login-form > h2").text
expected_Login_to_account = "Login to your account"

if Login_to_your_account == expected_Login_to_account:
    print("'Login to your account' is visible")
else:
    print("'Login to your account' is not visible")


# 6. Enter correct email address and password
driver.find_element(By.CSS_SELECTOR, ".login-form > form[method='post'] > input[name='email']").send_keys(email)
driver.find_element(By.CSS_SELECTOR, "form[method='post'] > input[name='password']").send_keys(password)


# 7. Click 'login' button
driver.find_element(By.CSS_SELECTOR, ".login-form > form[method='post'] > .btn.btn-default").click()


# 8. Verify that 'Logged in as username' is visible
logged_in_as_message = driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(10) > a").text
expected_logged_in_as_message = "Logged in as " + name
if logged_in_as_message == expected_logged_in_as_message:
    print("'Logged in as " "'" + name + "'"" is visible")
else:
    print("'Logged in as username' is not visible")

# 9. Click 'Logout' button
driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(4) > a").click()


# 10. Verify that user is navigated to login page
Login_to_your_account = driver.find_element(By.CSS_SELECTOR, ".login-form > h2").text
expected_Login_to_account = "Login to your account"

if Login_to_your_account == expected_Login_to_account:
    print("As 'Login to your account' is visible, it is verified that we have navigated to login page")
else:
    print("As 'Login to your account' is not visible, it is verified that we have navigated to login page")
