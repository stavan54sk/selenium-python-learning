from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

service=ChromeService("C://Users//DELL//Desktop//chromedriver.exe")
chromedriver=webdriver.Chrome(service=service)
chromedriver.get("https://www.google.com")
# chromedriver.maximize_window()

# firefoxService=FirefoxService()
# webdriver.FirefoxService(service=firefoxService)
# firefoxdriver=webdriver.Firefox()
# firefoxdriver.get("www.google.com")
# firefoxdriver.maximize_window()