import time

import selenium.webdriver.support.select
from select import select
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement
from selenium.webdriver.support.ui import Select

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

# 5. Verify 'New User Signup!' is visible
new_user_signup_message = driver.find_element(By.CSS_SELECTOR, ".signup-form > h2").text
expected_signup_message = "New User Signup!"

if new_user_signup_message == expected_signup_message:
    print("New user sign up message is visible")
else:
    print("New user sign up message is not visible")


# 6. Enter name and already registered email address
driver.find_element(By.CSS_SELECTOR, "form[method='post'] > input[name='name']").send_keys(name)
driver.find_element(By.CSS_SELECTOR, ".signup-form > form[method='post'] > input[name='email']").send_keys(email)


# 7. Click 'Signup' button
driver.find_element(By.CSS_SELECTOR, ".signup-form > form[method='post'] > .btn.btn-default").click()


# 8. Verify error 'Email Address already exist!' is visible
email_already_exist = driver.find_element(By.CSS_SELECTOR, ".signup-form > form[method='post'] > p").text
expected_message = "Email Address already exist!"

if email_already_exist == expected_message:
    print("'Email Address already exist!' message is visible")
else:
    print("'Email Address already exist!' message is not visible")
