# fight 500 - 1000
# economy class
# within 7 days
# 1 kg extra baggage
# ticket 1
# Expected cost: 105

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()

wait = WebDriverWait(driver, 30)

driver.get("https://muntasir101.github.io/Ticket-Fare/")

distance = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "input#distance"))
)
distance.send_keys("800")

departure_date = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "input#departureDate"))
)
departure_date.send_keys("2024-08-20")

service_class = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "select#serviceClass"))
)

service_class_options = Select(service_class)
service_class_options.select_by_value("economy")

number_of_tickets = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "input#numberOfTickets"))
)
number_of_tickets.send_keys("1")

extra_baggage = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "input#extraBaggage"))
)
extra_baggage.send_keys("1")

calculate_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "form#flightForm > button[type='button']"))
)
calculate_button.click()


# validate ticket price
expected_price = "Total Cost: $106.00"

actual_cost = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "div#result"))
).text

if expected_price == actual_cost:
    print("Test Passed")
else:
    print("Test Failed.Actual Cost: ", actual_cost, "But Expected: ", expected_price)
