import time
from csv import excel
from logging import exception

from selenium.common import NoSuchElementException, NoAlertPresentException, NoSuchWindowException, \
    NoSuchFrameException, InvalidArgumentException, ElementNotInteractableException, ElementClickInterceptedException, \
    StaleElementReferenceException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


chrome_driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome_driver.maximize_window()
chrome_driver.get('https://bonigarcia.dev/selenium-webdriver-java/web-form.html')

# NoSuchElementException
# try:
#     chrome_driver.find_element(By.CSS_SELECTOR, '#loginsdf')
# except NoSuchElementException:
#     print("NO SUCH ELEMENT EXCEPTION")

# NoAlertPresentException
# try:
#     chrome_driver.switch_to.alert.accept()
# except NoAlertPresentException:
#     print("NO ALERT PRESENT")

# NoSuchWindowException
# try:
#     chrome_driver.switch_to.window("test")
# except NoSuchWindowException:
#     print("NO SUCH WINDOW EXCEPTION")

# NoSuchFrameException
# try:
#     chrome_driver.switch_to.frame('test')
# except NoSuchFrameException:
#     print("NO SUCH FRAME EXCEPTION")

# InvalidArgumentException
# try:
#     chrome_driver.get('sdfsf')
# except InvalidArgumentException:
#     print("INVALID ARGUMENT EXCEPTION")

# ElementNotInteractableException
# try:
#     chrome_driver.find_element(By.CSS_SELECTOR, '[name="my-hidden"]').click()
# except ElementNotInteractableException:
#     print("ELEMENT NOT INTERACTABLE EXCEPTION")

# ElementClickInterceptedException
# try:
#     chrome_driver.find_element(By.CSS_SELECTOR, '[name="my-readonly"]').click()
# except ElementClickInterceptedException:
#     print("ELEMENT CLICK INTERCEPTED EXCEPTION")

# StaleElementReferenceException
# try:
#     chrome_driver.refresh()
#     time.sleep(5)
#     chrome_driver.find_element(By.CSS_SELECTOR, '[name="my-readonly"]').click()
# except StaleElementReferenceException:
#     print("STALE ELEMENT REFERENCE EXCEPTION")

# ElementNotVisibleException
# try:
#     chrome_driver.refresh()
#     time.sleep(5)
#     chrome_driver.find_element(By.CSS_SELECTOR, '[name="my-readonly"]').click()
# except ElementNotVisibleException:
#     print("STALE ELEMENT REFERENCE EXCEPTION")

# ElementNotSelectableException
# try:
#     chrome_driver.refresh()
#     time.sleep(5)
#     chrome_driver.find_element(By.CSS_SELECTOR, '[name="my-readonly"]').click()
# except ElementNotSelectableException:
#     print("STALE ELEMENT REFERENCE EXCEPTION")




# | **Exception**                      | **Example Scenario**                                            | **Handling Strategy**                                            |
# | ---------------------------------- | --------------------------------------------------------------- | ---------------------------------------------------------------- |
# | `NoSuchElementException`           | Locator not found, element not yet rendered                     | Use correct locator, apply waits (`WebDriverWait`)               |
# | `NoAlertPresentException`          | Trying to `accept()` or `dismiss()` alert when none exists      | Ensure alert is present (`expected_conditions.alert_is_present`) |
# | `NoSuchWindowException`            | Switching to a closed/non-existent tab                          | Verify available windows before switching                        |
# | `NoSuchFrameException`             | Switching to missing frame/iframe                               | Wait until frame is available, use correct name/index            |
# | `InvalidArgumentException`         | Bad URL in `driver.get()`, wrong file path, invalid JS argument | Validate input before calling method                             |
# | `StaleElementReferenceException`   | DOM refreshed, old element reference invalid                    | Re-locate element after DOM update                               |
# | `UnreachableBrowserException`      | Browser crash or connection lost                                | Restart browser session, add retry mechanism                     |
# | `TimeoutException`                 | Page load or wait exceeded set timeout                          | Increase timeout, add explicit waits                             |
# | `ScriptTimeoutException`           | JavaScript execution takes too long                             | Optimize script or increase script timeout                       |
# | `ElementNotVisibleException`       | Element in DOM but hidden                                       | Wait until element is visible                                    |
# | `ElementNotSelectableException`    | Element disabled/unselectable                                   | Ensure element state is ready before action                      |
# | `ElementClickInterceptedException` | Another element overlays the target                             | Use waits, scroll into view, or resolve overlay issue            |
# | `WebDriverException`               | General fallback for WebDriver-related issues                   | Log error, restart session if needed                             |
