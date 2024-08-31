import time
from selenium import webdriver
from selenium.webdriver.common.by import By


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

# 4. Click on 'Contact Us' button
driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(8) > a").click()

# 5. Verify 'GET IN TOUCH' is visible
get_in_touch = driver.find_element(By.CSS_SELECTOR, ".contact-form > .text-center.title").text
expected_get_in_touch = "GET IN TOUCH"

if get_in_touch == expected_get_in_touch:
    print("'GET IN TOUCH' is visible")
else:
    print("'GET IN TOUCH' is not visible")

# 6. Enter name, email, subject and message
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys(name)
driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys(email)
driver.find_element(By.CSS_SELECTOR, "input[name='subject']").send_keys("query")
driver.find_element(By.CSS_SELECTOR, "textarea#message").send_keys("hello")
time.sleep(3)

# 7. Upload file
upload_element = driver.find_element(By.CSS_SELECTOR, "[name='upload_file']")
upload_element.send_keys("E:\\Offline_Batch_19\\Projects\Automation_pnt19\\Project2_AutomationExercise\\BS_Report.pdf")
time.sleep(3)

# 8. Click 'Submit' button
driver.find_element(By.CSS_SELECTOR, "input[name='submit']").click()

# 9. Click OK button
driver.switch_to.alert.accept()

# 10. Verify success message 'Success! Your details have been submitted successfully.' is visible
success_message = driver.find_element(By.CSS_SELECTOR, ".alert.alert-success.status").text
expected_success_message = "Success! Your details have been submitted successfully."

if success_message == expected_success_message:
    print("'Success! Your details have been submitted successfully.' is visible")
else:
    print("'Success! Your details have been submitted successfully.' is not visible")

# 11. Click 'Home' button and verify that landed to home page successfully
driver.find_element(By.CSS_SELECTOR, "span").click()

home_button_text = driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(1) > a").text
expected_home_button_text = "Home"

if home_button_text == expected_home_button_text:
    print("Home page is visible")
else:
    print("Home page is not visible")
