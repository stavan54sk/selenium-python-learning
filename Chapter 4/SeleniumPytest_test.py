import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def test_selenium_pytest_title_validation(get_driver):
   print("Title:",get_driver.title)
   time.sleep(5)
   heading=get_driver.find_element(By.XPATH,'//a[contains(text(),"Qafox.com")]').text
   assert heading.__contains__("fox")
   print("First Selenium Pytest")

def test_selenium_pytest__validation(get_driver):
   wait_chrome_driver = WebDriverWait(get_driver, 10)
   search_text=wait_chrome_driver.until(expected_conditions.presence_of_element_located((By.NAME,'search')))
   search_text.send_keys('asdsfsdf')
   search_button = get_driver.find_element(By.XPATH, '//*[@class="input-group-btn"]//button').click()
   search_result_text=wait_chrome_driver.until(expected_conditions.visibility_of_element_located((By.XPATH,'//h2/following-sibling::p')))
   assert search_result_text.text.__contains__('no product')
   print("Second Selenium Pytest")







