import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chromedriver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigation & Page Info
#get()
chromedriver.get("https://testautomationpractice.blogspot.com")
time.sleep(3)
# chromedriver.get("https://www.facebook.com")
# time.sleep(3)

#current_url
# print(type(chromedriver.current_url))

#title
# print(type(chromedriver.title))

#pagesource
# print(chromedriver.page_source)

# Element Location
#find_element
# element=chromedriver.find_element(By.NAME, "q")
# print(type(element))
# elements = chromedriver.find_elements(By.TAG_NAME, "a")
# print(type(elements))

#Navigation Management
# chromedriver.back()
# print(type(chromedriver.current_window_handle))
# print(chromedriver.current_window_handle)
# time.sleep(3)
# chromedriver.forward()
# print(chromedriver.current_window_handle)
# time.sleep(3)
# chromedriver.refresh()
# print(chromedriver.current_window_handle)
# time.sleep(3)

#Window Management
# print(chromedriver.current_window_handle)
# print(type(chromedriver.window_handles))

# Switch Context
# chromedriver.switch_to.alert.accept()
# chromedriver.switch_to.alert.dismiss()
# chromedriver.switch_to.alert.send_keys(Keys.DELETE)
# chromedriver.switch_to.window(chromedriver.window_handles[1])
# chromedriver.switch_to.frame(chromedriver.window_handles[1])


# Browser Management
# chromedriver.maximize_window()
# time.sleep(3)
# chromedriver.minimize_window()
# time.sleep(3)
# chromedriver.fullscreen_window()
# time.sleep(3)
# print(type(chromedriver.get_cookies()))
# print(chromedriver.get_cookies())
# chromedriver.delete_all_cookies()
# print(chromedriver.get_cookies())

#Disposal
# chromedriver.close()
# chromedriver.quit()







