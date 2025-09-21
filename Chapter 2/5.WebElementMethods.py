import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import getAttribute_js
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.core import driver

chromedriver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

chromedriver.get("https://demoqa.com/login")
# search_box=chromedriver.find_element(By.NAME,"q")
# search_box.send_keys("selenium")
#
# #clear
# search_box.clear()
# time.sleep(5)
#
# #sendkeys
# search_box.send_keys(Keys.SHIFT,"selenium")
# time.sleep(5)

#text
# about_link=chromedriver.find_element(By.XPATH,"//a[text()='About']")
# time.sleep(5)
# print(submit_button.text)
# time.sleep(5)

#tag
# time.sleep(5)
# about_link=chromedriver.find_element(By.XPATH,"//a[text()='About']")
# time.sleep(5)
# print(about_link.tag_name)

# get_attribute
# time.sleep(5)
# google_search_button=chromedriver.find_element(By.NAME,"btnK")
# print(google_search_button.get_attribute("value"))

#size
# time.sleep(5)
# google_search_button=chromedriver.find_element(By.XPATH,"//a[text()='About']")
# print(google_search_button.size)

#rect
# time.sleep(5)
# google_search_button=chromedriver.find_element(By.ID,"login")
# print(google_search_button.is_displayed())
# print(google_search_button.is_enabled())
# print(google_search_button.is_selected())





