import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# chrome_driver.set_window_size(1200, 900)
# chrome_driver.set_window_position(4000,2000)
# chrome_driver.get("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")
time.sleep(3)

# get_window_size
# print(chrome_driver.get_window_size())
# time.sleep(3)
# chrome_driver.maximize_window()
# print(chrome_driver.get_window_size())

# set_window_size
# chrome_driver.set_window_size(1200, 900)
# time.sleep(3)

# get_window_position
# print(chrome_driver.get_window_position())
# time.sleep(3)

# set_window_position
# chrome_driver.set_window_position(10000,2000)
time.sleep(3)


# Browser History
chrome_driver.get("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")
time.sleep(3)
chrome_driver.get("https://bonigarcia.dev/selenium-webdriver-java")
time.sleep(3)
chrome_driver.back()
time.sleep(3)
chrome_driver.forward()
time.sleep(3)
chrome_driver.refresh()

