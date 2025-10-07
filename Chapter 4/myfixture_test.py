import pytest


@pytest.fixture()
def before_and_after_test():
    print("Launch Application")
    print("Goto URL")
    yield
    print("Quit Browser")

def test_login(before_and_after_test):
   print("Login Test")

def test_home(before_and_after_test):
   print("Home Test")

def test_order(before_and_after_test):
   print("Order Test")

def test_summary(before_and_after_test):
   print("Summary Test")