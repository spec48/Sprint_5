from random import randint
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_5.locators import *


def generate_login_by_mask():
    return f'evgeniy{randint(1, 99999)}@ya.ru'

def generate_login_not_by_mask():
    return f'user_{randint(1, 9999)}.ru'

def fill_registration_form(driver, login, password):
    driver.find_element(*DoskaLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.
                                   element_to_be_clickable(DoskaLocators.NOT_ACCOUNT_BUTTON))
    driver.find_element(*DoskaLocators.NOT_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.
                                   element_to_be_clickable(DoskaLocators.CREATE_ACCOUNT_BUTTON))
    driver.find_element(*DoskaLocators.EMAIL_INPUT).send_keys(login)
    driver.find_element(*DoskaLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*DoskaLocators.SUBMIT_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*DoskaLocators.CREATE_ACCOUNT_BUTTON).click()
