import pytest
from selenium import webdriver
from utilities.config_reader import ConfigReader

@pytest.fixture(scope='module')
def setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()

    yield driver

    driver.close()
    driver.quit()

@pytest.fixture(scope='function')
def config():
    return ConfigReader()
