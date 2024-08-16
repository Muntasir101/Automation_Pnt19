from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.google.com")

expected_title = "Google"
actual_title = driver.title

try:
    # verify title
    assert expected_title == actual_title, f"Title Mismatch.Actual title: {actual_title}"
except Exception as e:
    print("Exception: %s" % e)

expected_url = "https://www.google.com/"
actual_url = driver.current_url

try:
    # verify url
    assert expected_url == actual_url, f"Url Mismatch.Actual url: {actual_url}"
except Exception as e:
    print("Exception: %s" % e)

driver.quit()