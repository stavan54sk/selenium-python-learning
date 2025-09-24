import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from webdriver_manager.chrome import ChromeDriverManager

service=Service(ChromeDriverManager().install())
chromeDriver=webdriver.Chrome(service=service)
chromeDriver.get("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")

#absolute_xpath
# time.sleep(5)
# abs_xpath_element=chromeDriver.find_element(By.XPATH,"(//html//body//div//input)[1]")
# abs_xpath_element.send_keys("TEXT")
# time.sleep(5)

#relative_xpath
# time.sleep(5)
# relative_xpath_element=chromeDriver.find_element(By.XPATH,"//*[@name='my-textarea']")
# relative_xpath_element.send_keys("TEXT")
# time.sleep(5)

#contains
# time.sleep(5)
# contains_xpath_element=chromeDriver.find_element(By.XPATH,"//*[contains(@id,'check-2')]")
# contains_xpath_element.click()
# time.sleep(5)

#starts-with
# time.sleep(5)
# starts_xpath_element=chromeDriver.find_element(By.XPATH,"//*[starts-with(@type,'submit')]")
# starts_xpath_element.click()
# time.sleep(5)

#ends-with
# time.sleep(5)
# ends_xpath_element=chromeDriver.find_element(By.XPATH,"//*[ends-with(@type,'submit')]")
# ends_xpath_element.click()
# time.sleep(5)

#text()
# time.sleep(5)
# text_xpath_element=chromeDriver.find_element(By.XPATH,"//*[text()='Submit']")
# text_xpath_element.click()
# time.sleep(5)

#child
# time.sleep(5)
# child_xpath_element=chromeDriver.find_element(By.XPATH,"//div/*[0]")
# child_xpath_element.click()
# time.sleep(5)

#or
# time.sleep(5)
# or_xpath_element=chromeDriver.find_element(By.XPATH,"//*[@class='form-control' or @name='my-text']")
# or_xpath_element.click()
# time.sleep(5)

# and
# and_xpath_element=chromeDriver.find_element(By.XPATH,"//*[@class='form-control' and @name='my-text']")
# and_xpath_element.click()
# time.sleep(5)

# and
# and_xpath_element=chromeDriver.find_element(By.XPATH,"//*[not(@id='form-control') and @name='my-text']")
# and_xpath_element.click()
# time.sleep(5)



# xpath axes
# ancestor
# time.sleep(5)
# ancestor_elements=chromeDriver.find_elements(By.XPATH,'//*[@id="my-text-id"]//ancestor::div//h1')
# for element in ancestor_elements:
#     print(element.text)

# descendant
# time.sleep(5)
# descendant_elements=chromeDriver.find_elements(By.XPATH,'//*[@class="container"]//descendant::input')
# for element in descendant_elements:
#     print(element.get_attribute('name'))

# parent
# time.sleep(5)
# parent_elements=chromeDriver.find_elements(By.XPATH,'//input[@name="my-readonly"]//parent::*')
# for element in parent_elements:
#     print(element.get_attribute('name'))

# child
# time.sleep(5)
# child_elements=chromeDriver.find_elements(By.XPATH,'//*[@class="container"]//child::input[@name="my-readonly"]')
# for element in child_elements:
#     print(element.get_attribute('name'))

#preceding-sibling
# time.sleep(5)
# preceding_sibling_elements=chromeDriver.find_elements(By.XPATH,'//label[contains(text(),"Textarea")]//preceding-sibling::*')
# for element in preceding_sibling_elements:
#     print(element.get_attribute('name'))

# following-sibling
# time.sleep(5)
# following_sibling_elements=chromeDriver.find_elements(By.XPATH,'//h3[contains(text(),"SDK")]//following-sibling::span')
# for element in following_sibling_elements:
#     print(element.get_attribute('name'))

# following
# time.sleep(5)
# following_elements=chromeDriver.find_elements(By.XPATH,'//label[contains(text(),"Textarea")]//following::label')
# for element in following_elements:
#     print(element.get_attribute('class'))

# preceding
# time.sleep(5)
# following_elements=chromeDriver.find_elements(By.XPATH,'//label[contains(text(),"Textarea")]//preceding::label')
# for element in following_elements:
#     print(element.get_attribute('class'))

# --- ByIdOrName ---
# file_input = chromeDriver.find_element(By.ID, "my-file") if chromeDriver.find_elements(By.ID, "my-file") \
#     else chromeDriver.find_element(By.NAME, "my-file")
# print("ByIdOrName → name:", file_input.get_attribute("name"))

# --- ByChained equivalent ---
# form = chromeDriver.find_element(By.TAG_NAME, "form")
# rows_in_form = form.find_elements(By.CLASS_NAME, "row")
# print("ByChained → rows inside form:", len(rows_in_form))
#
# # --- ByAll equivalent ---
# all_matches = chromeDriver.find_elements(By.TAG_NAME, "form") + chromeDriver.find_elements(By.CLASS_NAME, "row")
# print("ByAll → form + rows:", len(all_matches))

# Reference element
# 1. above() -> element above the link
# read_only = driver.find_element(locate_with("tag name", "input").above(link))
# print("Above link:", read_only.get_attribute("name"))  # my-readonly
#
# # 2. below() -> element below the link
# submit_btn = driver.find_element(locate_with("tag name", "button").below(link))
# print("Below link:", submit_btn.text)  # Submit
#
# # 3. toLeftOf() -> element left of the password field
# password = driver.find_element("name", "my-password")
# text_input = driver.find_element(locate_with("tag name", "input").to_left_of(password))
# print("Left of password:", text_input.get_attribute("name"))  # my-text
#
# # 4. toRightOf() -> element right of the text field
# right_of_text = driver.find_element(locate_with("tag name", "input").to_right_of(text_input))
# print("Right of text:", right_of_text.get_attribute("name"))  # my-password
#
# # 5. near() -> element near the checkbox
# checkbox = driver.find_element("id", "my-check-1")
# near_checkbox = driver.find_element(locate_with("tag name", "input").near(checkbox))
# print("Near checkbox:", near_checkbox.get_attribute("type"))  # checkbox or radio

