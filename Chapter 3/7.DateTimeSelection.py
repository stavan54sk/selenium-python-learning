import time
from csv import excel
from logging import exception

from selenium.common import NoSuchElementException, NoAlertPresentException, NoSuchWindowException, \
    NoSuchFrameException, InvalidArgumentException, ElementNotInteractableException, ElementClickInterceptedException, \
    StaleElementReferenceException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


chrome_driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome_driver.maximize_window()
chrome_driver.get('https://www.tutorialspoint.com/selenium/practice/date-picker.php ')
webdriver_wait=WebDriverWait(chrome_driver,10)
openCalendar=webdriver_wait.until(expected_conditions.visibility_of_element_located((By.ID, 'datetimepicker2')))
openCalendar.click()
year=webdriver_wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[contains(@class,'open')]//select//following-sibling::div//input")))
year.clear()
year.send_keys("2020")

month=Select(webdriver_wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[contains(@class,'open')]//select"))))
month.select_by_visible_text("June")


day=webdriver_wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "(//*[contains(@class,'open')]//select//following::span[@class='flatpickr-day'])["+"24"+"]")))
day.click()

hour=webdriver_wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[contains(@class,'open')]//select//following::input[@class='numInput flatpickr-hour']")))
hour.send_keys('12')

mins=webdriver_wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[contains(@class,'open')]//select//following::input[@class='numInput flatpickr-minute']")))
mins.send_keys('40')

ampm=webdriver_wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[contains(@class,'open')]//select//following::span[@title='Click to toggle']")))

if ampm.text.__contains__('AM'):
    ampm.click()

time.sleep(5)
