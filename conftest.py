import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import constants


@pytest.fixture()
def webdriver_init():
    return webdriver.Chrome()

