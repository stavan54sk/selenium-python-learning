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
chrome_driver.get('https://www.tutorialspoint.com/selenium/practice/webtables.php')
webdriver_wait=WebDriverWait(chrome_driver,10)
webtable_title=webdriver_wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH,'//tr[1]//th')))
i=1
for title in webtable_title:
    print(title.text,end=' ')
    i+=1

print()
webtable_rows=webdriver_wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH,'//tbody//tr')))
i=1
for trow in webtable_rows:
    webtable_datas = webdriver_wait.until(
        expected_conditions.presence_of_all_elements_located((By.XPATH, "//tbody//tr[" + str(i) + "]//td")))
    tdatas = trow.find_elements()
    j=1
    for tdata in webtable_datas:
        print(tdata.text,end=' ')
        j += 1
    i+=1
    print()