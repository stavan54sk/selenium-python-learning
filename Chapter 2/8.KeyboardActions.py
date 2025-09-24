import os
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

service=Service(ChromeDriverManager().install())
chromeDriver=webdriver.Chrome(service=service)
chromeDriver.get("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")


# clear
# time.sleep(5)
# actions_chain=ActionChains(chromeDriver)
# input_text = chromeDriver.find_element(By.NAME, "my-text")
# input_text.clear()

# send_keys
# input_text.send_keys("Hello World!")
# time.sleep(5)

#action_chain
# input_text.click()
# actions_chain.key_down(Keys.CONTROL).send_keys('a').send_keys('c').key_up(Keys.CONTROL).perform()
# text_area = chromeDriver.find_element(By.NAME, "my-textarea")
# text_area.click()
# actions_chain.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
# time.sleep(5)

#slider
# slider = chromeDriver.find_element(By.NAME, "my-range")
# print("Initial:", slider.get_attribute("value"))
#
# for _ in range(5):
#     slider.send_keys(Keys.ARROW_RIGHT)
#     time.sleep(2)
#
# print("Final:", slider.get_attribute("value"))
# time.sleep(3)

# file_upload
# time.sleep(3)
# file_input = chromeDriver.find_element(By.NAME, "my-file")
# file_path = os.path.abspath("C://Users//DELL//Desktop/PCEP.PNG")
# file_input.send_keys(file_path)
# time.sleep(3)
