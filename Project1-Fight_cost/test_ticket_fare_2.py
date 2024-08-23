from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import pytest

# defining test data
test_data = [
    ("500", "economy", "1", "1"),
    ("800", "business", "1", "1"),
    ("900", "first", "1", "1")
]


@pytest.fixture
def setup():
    driver = webdriver.Firefox()
    driver.get("https://muntasir101.github.io/Ticket-Fare/")
    yield driver
    driver.quit()


@pytest.mark.parametrize("distance_value, ticket_class, number_of_tickets, extra_baggage", test_data)
def test_calculate_fare(setup, distance_value, ticket_class, number_of_tickets, extra_baggage):
    # set distance_value
    distance = WebDriverWait(setup, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input#distance"))
    )
    distance.send_keys(distance_value)

    # set date
    departure_date = WebDriverWait(setup, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input#departureDate"))
    )
    departure_date.send_keys("2024-08-24")

    # set class
    service_class = WebDriverWait(setup, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "select#serviceClass"))
    )

    service_class_options = Select(service_class)
    service_class_options.select_by_value(ticket_class)

    # set number of tickets
    number_of_tickets_field = WebDriverWait(setup, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input#numberOfTickets"))
    )
    number_of_tickets_field.send_keys(number_of_tickets)

    # set extra baggage
    extra_baggage_field = WebDriverWait(setup, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input#extraBaggage"))
    )
    extra_baggage_field.send_keys(extra_baggage)

    # calculate
    calculate_button = WebDriverWait(setup, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "form#flightForm > button[type='button']"))
    )
    calculate_button.click()
