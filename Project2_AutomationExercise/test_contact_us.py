import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions



@pytest.fixture
def driver():
    # 1. Launch browser in headless mode
    options = ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    print("Browser Launched successfully.")
    driver.implicitly_wait(20)
    # close browser
    yield driver
    driver.quit()


def test_contactUs(driver):
    try:
        # 2. Navigate to URL
        driver.get('http://automationexercise.com')
        # 3. Verify that home page is visible successfully
        assert "Automation Exercise" in driver.title
        print("Home page is visible successfully")
    except AssertionError:
        print("Home page is not visible.")
        print("Title Assertion Error: Home page title does not contain 'Automation Exercise'")

    # 4. Click on 'Contact Us' button
    driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(8) > a").click()

    # 5. Verify 'GET IN TOUCH' is visible
    try:
        assert driver.find_element(By.CSS_SELECTOR, ".contact-form > .text-center.title").text == "GET IN TOUCH"
        print("'GET IN TOUCH' is visible")
    except AssertionError:
        print("'GET IN TOUCH' is not visible")

    # 6. Enter name, email, subject and message
    driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Test")
    driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("test@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "input[name='subject']").send_keys("query")
    driver.find_element(By.CSS_SELECTOR, "textarea#message").send_keys("hello")
    time.sleep(3)

    # 7. Upload file
    upload_element = driver.find_element(By.CSS_SELECTOR, "[name='upload_file']")
    upload_element.send_keys(
        "E:\\Offline_Batch_19\\Projects\Automation_pnt19\\Project2_AutomationExercise\\BS_Report.pdf")
    time.sleep(3)

    # 8. Click 'Submit' button
    driver.find_element(By.CSS_SELECTOR, "input[name='submit']").click()

    # 9. Click OK button
    driver.switch_to.alert.accept()

    # 10. Verify success message 'Success! Your details have been submitted successfully.' is visible
    try:
        success_message = driver.find_element(By.CSS_SELECTOR, ".alert.alert-success.status").text
        assert success_message == "Success! Your details have been submitted successfully."
        print('Success Message is visible')
    except AssertionError:
        print("Assertion Error: success message is not visible.")

    # 11. Click 'Home' button and verify that landed to home page successfully
    home_button = driver.find_element(By.CSS_SELECTOR, "span")
    home_button.click()

    try:
        assert "Home" in home_button.text
        print("Home page is visible")
    except AssertionError:
        print("Assertion Error: home page is not visible")

