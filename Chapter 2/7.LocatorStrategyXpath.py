import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service=Service(ChromeDriverManager().install())
chromeDriver=webdriver.Chrome(service=service)
chromeDriver.get("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")

#absolute_xpath
# time.sleep(5)
# abs_xpath_element=chromeDriver.find_element(By.XPATH,"(//html//body//div//input)[1]")
# abs_xpath_element.send_keys("TEXT")
# time.sleep(5)

#relative_xpath
# time.sleep(5)
# relative_xpath_element=chromeDriver.find_element(By.XPATH,"//*[@name='my-textarea']")
# relative_xpath_element.send_keys("TEXT")
# time.sleep(5)

#contains
# time.sleep(5)
# contains_xpath_element=chromeDriver.find_element(By.XPATH,"//*[contains(@id,'check-2')]")
# contains_xpath_element.click()
# time.sleep(5)

#starts-with
# time.sleep(5)
# starts_xpath_element=chromeDriver.find_element(By.XPATH,"//*[starts-with(@type,'submit')]")
# starts_xpath_element.click()
# time.sleep(5)

#ends-with
# time.sleep(5)
# ends_xpath_element=chromeDriver.find_element(By.XPATH,"//*[ends-with(@type,'submit')]")
# ends_xpath_element.click()
# time.sleep(5)

#text()
# time.sleep(5)
# text_xpath_element=chromeDriver.find_element(By.XPATH,"//*[text()='Submit']")
# text_xpath_element.click()
# time.sleep(5)

#child
# time.sleep(5)
# child_xpath_element=chromeDriver.find_element(By.XPATH,"//div/*[0]")
# child_xpath_element.click()
# time.sleep(5)

#or
# time.sleep(5)
# or_xpath_element=chromeDriver.find_element(By.XPATH,"//*[@class='form-control' or @name='my-text']")
# or_xpath_element.click()
# time.sleep(5)

# and
# and_xpath_element=chromeDriver.find_element(By.XPATH,"//*[@class='form-control' and @name='my-text']")
# and_xpath_element.click()
# time.sleep(5)

# and
# and_xpath_element=chromeDriver.find_element(By.XPATH,"//*[not(@id='form-control') and @name='my-text']")
# and_xpath_element.click()
# time.sleep(5)