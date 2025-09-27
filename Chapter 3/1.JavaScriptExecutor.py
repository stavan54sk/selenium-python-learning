import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome_driver.maximize_window()
chrome_driver.get("https://bonigarcia.dev/selenium-webdriver-java/infinite-scroll.html")

# window.scrollBy(0,1000)
# chrome_driver.execute_script("window.scrollBy(0,1000)")
# time.sleep(5)


# arguments[0].scrollIntoView()
# chrome_driver.execute_script('arguments[0].scrollIntoView()',chrome_driver.find_element(By.XPATH,'//a[contains(text(),"Boni")]'))
# time.sleep(5)


# arguments[0].setAttribute('value',arguments[1]),webElement,00000
# time.sleep(3)
# chrome_driver.execute_script("arguments[0].setAttribute('value',arguments[1])",chrome_driver.find_element(By.CSS_SELECTOR,'[name="my-colors"]'),'#FFFF00')
# time.sleep(3)

# arguments[0].click()
# time.sleep(3)
# # chrome_driver.find_element(By.XPATH,'//a[contains(text(),"Boni")]').click()
# chrome_driver.execute_script('arguments[0].click()',chrome_driver.find_element(By.XPATH,'//a[contains(text(),"Boni")]'))
# time.sleep(3)


# time.sleep(3)
# chrome_driver.set_page_load_timeout(1)  # 1 sec timeout
# try:
#     chrome_driver.get("https://bonigarcia.dev/selenium-webdriver-java/")
# except TimeoutException:
#     time.sleep(3)
#     print("✅ Timeout exception occurred as expected")


# | Situation                                                           | Why `.click()` fails                                                              | Why JS helps                                                                  |
# | ------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
# | **Element hidden by overlay / popup / banner**                      | Selenium won’t click hidden elements (throws `ElementClickInterceptedException`). | JS click bypasses visibility check.                                           |
# | **Element outside viewport (needs scrolling)**                      | Selenium might throw `ElementNotInteractableException`.                           | JS click forces the event without scrolling.                                  |
# | **Custom UI elements (e.g., styled checkboxes, hidden `<input>`s)** | Selenium can’t directly interact if it’s hidden behind a custom design.           | JS can trigger the click directly on the hidden element.                      |
# | **Slow rendering / async DOM updates**                              | Selenium finds element but can’t interact yet.                                    | JS click can sometimes bypass timing issues (though explicit wait is better). |
# | **Non-standard click handlers**                                     | Some apps rely only on JS event listeners (`onclick`) rather than native clicks.  | JS directly invokes those handlers.                                           |




