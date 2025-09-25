from wsgiref.simple_server import server_version

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


chromedriver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chromedriver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
chromedriver.maximize_window()

# implicitly_wait
chromedriver.implicitly_wait(10)
# landscape=chromedriver.find_element(By.CSS_SELECTOR, '[src="img/landscape.png"]')
# print(landscape.is_displayed())

# explicit_wait
# chromedriver_wait=WebDriverWait(chromedriver,10)
# chromedriver_wait.until(expected_conditions.element_to_be_clickable((By.XPATH,'//span[text()="8"]'))).click()
# chromedriver_wait.until(expected_conditions.element_to_be_clickable((By.XPATH,'//span[text()="+"]'))).click()
# chromedriver_wait.until(expected_conditions.element_to_be_clickable((By.XPATH,'//span[text()="1"]'))).click()
# chromedriver_wait.until(expected_conditions.element_to_be_clickable((By.XPATH,'//span[text()="="]'))).click()
# chromedriver_wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR,'[class="screen"]'),'9'))

# #fluent_wait
# chromedriver_wait=WebDriverWait(
#     chromedriver,
#     10,
#     2,
#     [NoSuchElementException]
#     )
#
# chromedriver_wait.until(expected_conditions.element_to_be_clickable((By.XPATH,'//span[text()="8"]'))).click()
# chromedriver_wait.until(expected_conditions.element_to_be_clickable((By.XPATH,'//span[text()="+"]'))).click()
# chromedriver_wait.until(expected_conditions.element_to_be_clickable((By.XPATH,'//span[text()="1"]'))).click()
# chromedriver_wait.until(expected_conditions.element_to_be_clickable((By.XPATH,'//span[text()="="]'))).click()
# chromedriver_wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR,'[class="screen"]'),'9'))