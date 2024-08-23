from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import pytest


@pytest.mark.parametrize(
    "distance_value", "number_of_tickets", "extra_baggage",
    [
        ("800", "1", "1"),
        ("800", "2", "2"),
        ("900", "1", "1")
    ])
def test_ticket_cost(distance_value, number_of_tickets, extra_baggage):
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 30)

    try:
        driver.get("https://muntasir101.github.io/Ticket-Fare/")

        # set distance_value
        distance = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input#distance"))
        )
        distance.send_keys(distance_value)

        # set date
        departure_date = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input#departureDate"))
        )
        departure_date.send_keys("2024-08-24")

        # set class
        service_class = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "select#serviceClass"))
        )

        service_class_options = Select(service_class)
        service_class_options.select_by_value("economy")

        # set number of tickets
        number_of_tickets_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input#numberOfTickets"))
        )
        number_of_tickets_field.send_keys(number_of_tickets)

        # set extra baggage
        extra_baggage_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input#extraBaggage"))
        )
        extra_baggage_field.send_keys(extra_baggage)

        # calculate
        calculate_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "form#flightForm > button[type='button']"))
        )
        calculate_button.click()

    finally:
        driver.quit()
