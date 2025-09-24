import math
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


service=Service(ChromeDriverManager().install())
chromeDriver=webdriver.Chrome(service=service)
chromeDriver.get("https://bonigarcia.dev/selenium-webdriver-java/draw-in-canvas.html")

#actions_click
# time.sleep(3)
# actions_chain=ActionChains(chromeDriver)
# actions_chain.click(chromeDriver.find_element(By.CSS_SELECTOR,'[id="my-dropdown-1"]')).perform()
# time.sleep(3)

#actions_context_click
# time.sleep(3)
# actions_chain=ActionChains(chromeDriver)
# actions_chain.context_click(chromeDriver.find_element(By.CSS_SELECTOR,'[id="my-dropdown-2"]')).perform()
# time.sleep(3)
# chromeDriver.find_element(By.XPATH,'(//a[contains(text(),"Separated link")])[2]').click()
# time.sleep(3)

#actions_double_click
# time.sleep(3)
# actions_chain=ActionChains(chromeDriver)
# actions_chain.double_click(chromeDriver.find_element(By.CSS_SELECTOR,'[id="my-dropdown-3"]')).perform()
# time.sleep(3)
# chromeDriver.find_element(By.XPATH,'(//a[contains(text(),"Separated link")])[3]').click()
# time.sleep(3)

#actions_mouse_over
# time.sleep(3)
# actions_chain=ActionChains(chromeDriver)
# actions_chain.move_to_element(chromeDriver.find_element(By.XPATH,'//*[contains(@src,"calendar")]')).perform()
# time.sleep(3)
# print(chromeDriver.find_element(By.XPATH,'//p[text()="Calendar"]').is_displayed())
# time.sleep(3)

#actions_mouse_over
# time.sleep(3)
# draggable = chromeDriver.find_element(By.ID, "draggable")
# target = chromeDriver.find_element(By.ID, "target")
# time.sleep(3)
# actions_chain=ActionChains(chromeDriver)
# actions_chain.drag_and_drop(draggable,target).perform()
# time.sleep(3)

# time.sleep(3)
# actions_chain=ActionChains(chromeDriver)
# draggable = chromeDriver.find_element(By.ID, "draggable")
# actions_chain.drag_and_drop_by_offset(draggable, 100, 0)\
#        .drag_and_drop_by_offset(draggable, 0, 100)\
#        .drag_and_drop_by_offset(draggable, -100, 0)\
#        .drag_and_drop_by_offset(draggable, 0, -100)\
#        .perform()
# time.sleep(3)

time.sleep(3)
action_chain = ActionChains(chromeDriver)
canvas=chromeDriver.find_element(By.CSS_SELECTOR, "[id='my-canvas']")
action_chain.click_and_hold(canvas).perform()

points=10
radius=15
for i in range(points+1):
    radian=math.radians(360*i/points)
    x=int(math.cos(radian)*radius)
    y=int(math.sin(radian)*radius)
    action_chain.move_by_offset(x,y).perform()
