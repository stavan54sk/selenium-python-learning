import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service=Service(ChromeDriverManager().install())
chromeDriver=webdriver.Chrome(service=service)
chromeDriver.get("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")

# css_selector by id
# time.sleep(5)
# check_box = chromeDriver.find_element(By.CSS_SELECTOR, "#my-check-2")

# css_selector by class
# time.sleep(5)
# form_controls = chromeDriver.find_elements(By.CSS_SELECTOR, ".form-control")
# time.sleep(5)

# tag+id
# time.sleep(5)
# chromeDriver.find_element(By.CSS_SELECTOR, "input#my-text-id").send_keys("TEST")
# time.sleep(5)

# tag+class
# time.sleep(5)
# chromeDriver.find_element(By.CSS_SELECTOR, "textarea.form-control").send_keys("TEXT AREA TEXT")
# time.sleep(5)

#attribute exact match
# time.sleep(5)
# chromeDriver.find_element(By.CSS_SELECTOR, "input[id='my-check-2']").click()
# time.sleep(5)

#attribute contains
# time.sleep(5)
# chromeDriver.find_element(By.CSS_SELECTOR, "input[id*='check-2']").click()
# time.sleep(5)

#grouping
# divs_and_spans = driver.find_elements(By.CSS_SELECTOR, "div, span")

#descendant
# spans_in_div = driver.find_elements(By.CSS_SELECTOR, "div span")

#child
# list_items = driver.find_elements(By.CSS_SELECTOR, "ul > li")

#sibling
# spans_after_p = driver.find_elements(By.CSS_SELECTOR, "p ~ span")

#adjacent sibling
# p_after_h2 = driver.find_element(By.CSS_SELECTOR, "h2 + p")

#nth-child ---
# second_paragraph = driver.find_element(By.CSS_SELECTOR, "p:nth-child(2)")

#nth-last-child
# second_from_last_paragraph = driver.find_element(By.CSS_SELECTOR, "p:nth-last-child(2)")




