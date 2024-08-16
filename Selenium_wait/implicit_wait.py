from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.implicitly_wait(10)

driver.get("https://tutorialsninja.com/demo/")

my_account = driver.find_element(By.CSS_SELECTOR, ".list-inline .dropdown .hidden-md")
my_account.click()

Login = driver.find_element(By.LINK_TEXT, "Login")
Login.click()


Email = driver.find_element(By.CSS_SELECTOR, "#input-email")

Email_is_enabled_status = Email.is_enabled()
Email_is_displayed_status = Email.is_displayed()

if Email_is_enabled_status and Email_is_displayed_status:
    Email.clear()
    Email.send_keys("mail123@gmail.com")
else:
    print("Email is not enabled and not displayed")

Password = driver.find_element(By.CSS_SELECTOR, "#input-password")
Password.clear()
Password.send_keys("12345645")

Login_btn = driver.find_element(By.CSS_SELECTOR, "[action] .btn-primary")
Login_btn_is_displayed_status = Login_btn.is_displayed()
Login_btn_is_enabled_status = Login_btn.is_enabled()

if Login_btn_is_displayed_status and Login_btn_is_enabled_status:
    Login_btn.click()
else:
    print('Login button not enabled and not displayed')

# verify error message
expected_error_message = "Warning: No match for E-Mail Address and/or Password."

actual_error_message = driver.find_element(By.CSS_SELECTOR, ".alert-dismissible").text

error_message_font_size = driver.find_element(By.CSS_SELECTOR, ".alert-dismissible").value_of_css_property("font-size")
print("Error Message font_size:", error_message_font_size)

if actual_error_message != expected_error_message:
    print("Error message mismatch")
else:
    print("Error Message verified.")

driver.quit()