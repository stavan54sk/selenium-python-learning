from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options=Options()
options.add_argument('--headless')

chromedriver=webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    options=options
)

