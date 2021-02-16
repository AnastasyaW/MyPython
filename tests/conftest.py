import pytest
from selenium import webdriver

# we need to declare the driver at the class lever
# >
driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
# "request" is an instance for the fixture that comes by default
#  we user request to sent the driver to the TC_class
def setUp(request):
    # we initialize a global driver
    global driver
    browserName = request.config.getoption("browser_name")
    if browserName == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\WorkQA\\chromedriver.exe")
    elif browserName == "firefox":
        driver = webdriver.Chrome(executable_path="C:\\WorkQA\\geckodriver.exe")
    elif browserName == "IE":
        driver = webdriver.Chrome(executable_path="C:\\WorkQA\\IEdriver.exe")
    driver.get("https://www.rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    #  do send the driver to our test class we use this:
    request.cls.driver = driver
    yield
    driver.close()


7