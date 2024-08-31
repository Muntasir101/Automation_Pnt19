import time

import selenium.webdriver.support.select
from select import select
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement
from selenium.webdriver.support.ui import Select
from faker import Faker
fake = Faker()

# initial info
name = "Ron Wisley"
# email = "riyak8584333@avashost.com"
email = fake.email()
password = "121212"
company = "People and Tech"
address = "223/B, baker Street, East London"
address2 = "44/6, new york, USA"

# 1. Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

def account_creation():
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


# 6. Enter name and email address & 7. Click 'Signup' button
    driver.find_element(By.CSS_SELECTOR, "form[method='post'] > input[name='name']").send_keys(name)
    driver.find_element(By.CSS_SELECTOR, ".signup-form > form[method='post'] > input[name='email']").send_keys(email)
    driver.find_element(By.CSS_SELECTOR, ".signup-form > form[method='post'] > .btn.btn-default").click()


# 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
    new_account_info_message = driver.find_element(By.CSS_SELECTOR, ".login-form > .text-center.title > b").text
    expected_account_info_message = "ENTER ACCOUNT INFORMATION"

    if new_account_info_message == expected_account_info_message:
        print("'ENTER ACCOUNT INFORMATION' is visible")
    else:
        print("'ENTER ACCOUNT INFORMATION' is not visible")


# 9. Fill details: Title, Name, Email, Password, Date of birth
    driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(1) > .top > .radio  input[name='title']").click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 200)")
    password_box = driver.find_element(By.CSS_SELECTOR, "input#password")
    password_box.send_keys(password)

#day
    day = driver.find_element(By.CSS_SELECTOR, "select#days")
    day = Select(day)
    day.select_by_index(6)
#month
    month = driver.find_element(By.CSS_SELECTOR, "select#months")
    month = Select(month)
    month.select_by_index(3)
#year
    year = driver.find_element(By.CSS_SELECTOR, "select#years")
    year = Select(year)
    year.select_by_visible_text("1997")


# 10. Select checkbox 'Sign up for our newsletter!
    driver.find_element(By.CSS_SELECTOR, "input#newsletter").click()


# 11. Select checkbox 'Receive special offers from our partners!'
    driver.find_element(By.CSS_SELECTOR, "input#optin").click()


# 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    #F name
    driver.find_element(By.CSS_SELECTOR, "input#first_name").send_keys(name.split(" ")[0])
    #Lname
    driver.find_element(By.CSS_SELECTOR, "input#last_name").send_keys((name.split(" ")[1]))
    #company
    driver.find_element(By.CSS_SELECTOR, "input#company").send_keys(company)
    #address
    driver.find_element(By.CSS_SELECTOR, "input[name='address1']").send_keys(address)
    #address2
    driver.find_element(By.CSS_SELECTOR, "input[name='address2']").send_keys(address2)
    #country
    country_button = driver.find_element(By.CSS_SELECTOR, "select#country")
    country_button = Select(country_button)
    country_button.select_by_visible_text("United States")
    #state
    driver.find_element(By.CSS_SELECTOR, "input#state").send_keys("New York")
    #city
    driver.find_element(By.CSS_SELECTOR, "input#city").send_keys("New York")
    #zip code
    driver.find_element(By.CSS_SELECTOR, "input#zipcode").send_keys("101")
    #Mobile number
    driver.find_element(By.CSS_SELECTOR, "input#mobile_number").send_keys("09856")


# 13. Click 'Create Account button'
    driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-default']").click()

account_creation()

# 14. Verify that 'ACCOUNT CREATED!' is visible
account_created_text = driver.find_element(By.CSS_SELECTOR, ".text-center.title > b").text
expected_account_created_message = 'ACCOUNT CREATED!'

if account_created_text == expected_account_created_message:
    print("'ACCOUNT CREATED!' is visible")
else:
    print("'ACCOUNT CREATED!' is not visible")


# 15. Click 'Continue' button
driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()


# 16. Verify that 'Logged in as username' is visible
logged_in_as_message = driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(10) > a").text
expected_logged_in_as_message = "Logged in as " + name
if logged_in_as_message == expected_logged_in_as_message:
    print("'Logged in as " "'" + name + "'"" is visible")
else:
    print("'Logged in as username' is not visible")


# 17. Click 'Delete Account' button
driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(5) > a").click()


# 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
account_deleted_message = driver.find_element(By.CSS_SELECTOR, ".text-center.title > b").text
expected_account_deleted_message = 'ACCOUNT DELETED!'
if account_deleted_message == expected_account_deleted_message:
    print("'ACCOUNT DELETED!' is visible")
else:
    print("'ACCOUNT DELETED!' is not visible")

driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()





