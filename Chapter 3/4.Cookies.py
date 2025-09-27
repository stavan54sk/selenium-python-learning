import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# get_cookies
# chrome_driver.get("https://bonigarcia.dev/selenium-webdriver-java/cookies.html")
# time.sleep(3)
# print(chrome_driver.get_cookies())

# get_cookie
# chrome_driver.get("https://bonigarcia.dev/selenium-webdriver-
# java/cookies.html")
# time.sleep(3)
# print(chrome_driver.get_cookie('username')['value'])
# print(chrome_driver.get_cookie('username')['value'])

# add_cookie
# chrome_driver.get("https://bonigarcia.dev/selenium-webdriver-java/cookies.html")
# time.sleep(3)
# chrome_driver.add_cookie({'name': 'mycookie', 'value': 'mycookievalue'})
# print(chrome_driver.get_cookie('mycookie')['name'])
# print(chrome_driver.get_cookie('mycookie')['value'])

# add_cookie/edit_cookie
# chrome_driver.get("https://bonigarcia.dev/selenium-webdriver-java/cookies.html")
# time.sleep(3)
# print("Before Cookie",chrome_driver.get_cookie('username')['value'])
# chrome_driver.add_cookie({'name': 'username', 'value': 'newnamecookievalue'})
# time.sleep(3)
# print("After Cookie",chrome_driver.get_cookie('username')['value'])

# delete_cookie/edit_cookie
chrome_driver.get("https://bonigarcia.dev/selenium-webdriver-java/cookies.html")
time.sleep(3)
print("Before Cookie",chrome_driver.get_cookie('username')['value'])
chrome_driver.add_cookie({'name': 'username', 'value': 'newnamecookievalue'})
time.sleep(3)
print("After Cookie",chrome_driver.get_cookie('username')['value'])
time.sleep(3)
chrome_driver.delete_cookie('username')
time.sleep(3)
print("After Cookie",chrome_driver.get_cookie('username'))