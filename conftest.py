import pytest
from selenium import webdriver
from utilities.config_reader import ConfigReader

@pytest.fixture(scope='function')
def setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()

    yield driver

    driver.close()
    driver.quit()

# Setup function with 'session' scope for Address Test cases
@pytest.fixture(scope='session')
def setup_function():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()

    yield driver

    driver.close()
    driver.quit()

@pytest.fixture(scope='function')
def config():
    return ConfigReader()
