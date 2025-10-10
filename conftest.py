# import pytest
# @pytest.fixture(scope="session")
# def before_and_after_test():
#     print("Launch Application")
#     print("Goto URL")
#     yield
#     print("Quit Browser")
#
import pytest

# @pytest.fixture(autouse=True)
# def before_and_after_test():
#     print("Launch Application")
#     print("Goto URL")
#     yield
#     print("Quit Browser")

@pytest.fixture(scope="session",autouse=True)
def before_and_after_test():
    print("Session Launch Application")
    print("Session Goto URL")
    yield
    print("Session Quit Browser")

# @pytest.fixture(scope="function",autouse=True)
# def before_and_after_function():
#     print("Before Function")
#     yield
#     print("After Function")