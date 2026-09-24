import pytest
from selenium import webdriver
from Sprint_5.urls import HOME_PAGE


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get(HOME_PAGE)
    yield driver
    driver.quit()
