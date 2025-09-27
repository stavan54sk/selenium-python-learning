import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

chrome_driver.get("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")
time.sleep(3)

# save_screenshot
# chrome_driver.save_screenshot('screenshot.png')
# time.sleep(3)

# get_screenshot_as_base64
# chrome_driver.get_screenshot_as_base64()
# print("✅ Base64 Screenshot (prefix with data:image/png;base64, to view)")
# time.sleep(3)

# get_screenshot_as_png
# screenshot_bytes = chrome_driver.get_screenshot_as_png()
# with open("screenshot_bytes.png", "wb") as f:
#     f.write(screenshot_bytes)

# screenshot
# header = chrome_driver.find_element(By.CSS_SELECTOR, '[class="row py-2"]')
# header.screenshot("header_screenshot.png")
# time.sleep(3)