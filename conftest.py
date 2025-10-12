from email.policy import default

import pytest
from execnet.gateway_base import serve
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="edge")
#
# @pytest.fixture(scope="session",autouse=True)
# def my_driver(request):
#     if request.config.getoption("--browser") == "chrome":
#             service=Service(ChromeDriverManager().install())
#             chrome_driver=webdriver.Chrome(service=service)
#             chrome_driver.maximize_window()
#             chrome_driver.get("https://tutorialsninja.com/demo/")
#             yield chrome_driver
#             chrome_driver.close()

# @pytest.fixture(autouse=True)
# def before_and_after_test():
#     print("Launch Application")
#     print("Goto URL")
#     yield
#     print("Quit Browser")

# @pytest.fixture(scope="function",autouse=True)
# def before_and_after_function():
#     print("Before Function")
#     yield
#     print("After Function")

# import pytest
# @pytest.fixture(scope="session")
# def before_and_after_test():
#     print("Launch Application")
#     print("Goto URL")
#     yield
#     print("Quit Browser")


import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser",default="edge")

@pytest.fixture(scope='session')
def get_browser(request):
    return request.config.getoption("browser").lower()

@pytest.fixture(scope='function')
def get_driver(request,get_browser):
    if get_browser == 'chrome':
        serve=Service(ChromeDriverManager().install())
        my_driver=webdriver.Chrome(service=serve)
        my_driver.maximize_window()
        my_driver.get("https://tutorialsninja.com/demo/")
        yield my_driver
        my_driver.quit()
    else:
        raise ValueError("Driver Not Found")



