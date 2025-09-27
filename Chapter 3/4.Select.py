import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


chrome_driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome_driver_wait=WebDriverWait(chrome_driver,10)
chrome_driver.get('https://bonigarcia.dev/selenium-webdriver-java/web-form.html')

my_select=chrome_driver.find_element(By.CSS_SELECTOR,'[name="my-select"]')
chrome_driver_wait.until(expected_conditions.visibility_of(my_select))
select=Select(my_select)


#options
# print(type(select.options))
# for element in select.options:
#     print(element.text)

# all_selected_options
# time.sleep(3)
# for element in select.all_selected_options:
#     print(element.text)]

# first_selected_option
# time.sleep(3)
# print(select.first_selected_option.text)

# select_by_visible_text
# time.sleep(3)
# select.select_by_visible_text('Two')
# time.sleep(3)

# select_by_value
# time.sleep(3)
# select.select_by_value('3')
# time.sleep(3)

# select_by_index
# time.sleep(3)
# select.select_by_index(3)
# time.sleep(3)

# deselect_by_index
# time.sleep(3)
# select.deselect_by_index(3)
# time.sleep(3)

# deselect_by_value
# time.sleep(3)
# select.deselect_by_value('3')
# time.sleep(3)

# deselect_by_value
# time.sleep(3)
# select.deselect_by_visible_text('Three')
# time.sleep(3)


datalist_input = chrome_driver.find_element(By.NAME, "my-datalist")
datalist_input.click()

# Locate an option inside <datalist>
option = chrome_driver.find_element(By.XPATH, "//datalist[@id='my-options']/option[2]")
option_value = option.get_attribute("value")

# Send option value to the input
datalist_input.send_keys(option_value)

print("Selected option:", option_value)
assert option_value == "New York"


