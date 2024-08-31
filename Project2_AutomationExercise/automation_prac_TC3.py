import time

import selenium.webdriver.support.select
from select import select
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement
from selenium.webdriver.support.ui import Select


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


# 5. Verify 'Login to your account' is visible
Login_to_your_account = driver.find_element(By.CSS_SELECTOR, ".login-form > h2").text
expected_Login_to_account = "Login to your account"

if Login_to_your_account == expected_Login_to_account:
    print("'Login to your account' is visible")
else:
    print("'Login to your account' is not visible")


# 6. Enter incorrect email address and password
driver.find_element(By.CSS_SELECTOR, ".login-form > form[method='post'] > input[name='email']").send_keys("wrongemail@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form[method='post'] > input[name='password']").send_keys("wrongpassword")


# 7. Click 'login' button
driver.find_element(By.CSS_SELECTOR, ".login-form > form[method='post'] > .btn.btn-default").click()


# 8. Verify error 'Your email or password is incorrect!' is visible
email_password_alert = driver.find_element(By.CSS_SELECTOR, ".login-form > form[method='post'] > p").text
expected_email_password_alert = "Your email or password is incorrect!"

if email_password_alert == expected_email_password_alert:
    print("'Your email or password is incorrect!' is visible")
else:
    print("'Your email or password is incorrect!' is not visible")




