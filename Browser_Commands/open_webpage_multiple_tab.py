from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
print(driver.get_window_size())  # {'width': 1296, 'height': 688}
driver.set_window_size(400, 200)

websites = [
    "http://google.com",
    "http://bbc.com",
    "http://apple.com",
    "http://cnn.com"
]

# open the first website
driver.get(websites[0])

# open each additional website in a new tab
for url in websites[1:]:
    # open new tab
    driver.execute_script("window.open('');")

    # switch to the new tab
    driver.switch_to.window(driver.window_handles[-1])

    driver.get(url)

# driver.close()
# driver.quit()
