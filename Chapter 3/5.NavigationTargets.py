import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


chrome_driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome_driver_wait=WebDriverWait(chrome_driver,10)
chrome_driver.get('https://bonigarcia.dev/selenium-webdriver-java/dialog-boxes.html')

# TABS
# new_window
# chrome_driver.switch_to.new_window(WindowTypes.TAB)
# chrome_driver.get('https://bonigarcia.dev/selenium-webdriver-java/web-form.html')
#
# # current_window_handle
# print(chrome_driver.current_window_handle)
# time.sleep(3)
#
# #window_handles
# for handle in chrome_driver.window_handles:
#     print(handle)
#     time.sleep(3)
# print(chrome_driver.current_window_handle)
#
# # switch_to.window
# time.sleep(3)
# chrome_driver.switch_to.window(chrome_driver.window_handles[0])
# print(chrome_driver.current_window_handle)
# time.sleep(3)

# WINDOWS
# chrome_driver.switch_to.new_window(WindowTypes.WINDOW)
# chrome_driver.get('https://bonigarcia.dev/selenium-webdriver-java/web-form.html')
# time.sleep(3)
#
# chrome_driver.switch_to.window(chrome_driver.window_handles[0])
# time.sleep(3)

#IFRAME
# myiframe=chrome_driver.find_element(By.XPATH, "//*[contains(@id,'my-iframe')]")
# # WebDriverWait(chrome_driver,10).until(expected_conditions.frame_to_be_available_and_switch_to_it('my-iframe'))
# time.sleep(3)
# chrome_driver.switch_to.frame(myiframe)
# time.sleep(3)
# print(chrome_driver.find_element(By.XPATH, "//*[contains(text(),'Lorem ipsum')]").text)
# time.sleep(3)


#FRAME
# myframe=chrome_driver.find_element(By.XPATH, "//frame[3]")
# # WebDriverWait(chrome_driver,10).until(expected_conditions.frame_to_be_available_and_switch_to_it('my-iframe'))
# time.sleep(3)
# chrome_driver.switch_to.frame(myframe)
# time.sleep(3)
# print(chrome_driver.find_element(By.XPATH, "//*[contains(text(),'Gar')]").text)
# time.sleep(3)

# ALERTS
# time.sleep(3)
# chrome_driver.find_element(By.CSS_SELECTOR,'[id="my-alert"]').click()
# time.sleep(3)
# WebDriverWait(chrome_driver,10).until(expected_conditions.alert_is_present())
# time.sleep(3)
# chrome_driver.switch_to.alert.accept()
# time.sleep(3)

# time.sleep(3)
# chrome_driver.find_element(By.CSS_SELECTOR,'[id="my-confirm"]').click()
# time.sleep(3)
# WebDriverWait(chrome_driver,10).until(expected_conditions.alert_is_present())
# time.sleep(3)
# chrome_driver.switch_to.alert.dismiss()
# time.sleep(3)

# time.sleep(3)
# chrome_driver.find_element(By.CSS_SELECTOR,'[id="my-prompt"]').click()
# time.sleep(3)
# WebDriverWait(chrome_driver,10).until(expected_conditions.alert_is_present())
# time.sleep(3)
# chrome_driver.switch_to.alert.send_keys("TESTFN TESTLN")
# time.sleep(3)

# time.sleep(3)
# chrome_driver.find_element(By.CSS_SELECTOR,'[id="my-modal"]').click()
# time.sleep(3)
# chrome_driver.find_element(By.XPATH,'//button[contains(text(),"Save")]').click()
# time.sleep(3)
# WebDriverWait(chrome_driver,10).until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR,'[id="modal-text"]'),'Save changes'))




