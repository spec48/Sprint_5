from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_5.urls import HOME_PAGE
from Sprint_5.helpers import generate_login_by_mask, fill_registration_form
from Sprint_5.locators import *
from Sprint_5.data import *


class TestUserAuthorization:

    def test_login_user_go_to_home_page(self, driver):
        user_login = generate_login_by_mask()
        fill_registration_form(driver, user_login, password)
        WebDriverWait(driver, 3).until(expected_conditions.
                                       visibility_of_element_located(DoskaLocators.USER_NAME))
        driver.find_element(*DoskaLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.
                                       element_to_be_clickable(DoskaLocators.LOGIN_AND_REGISTRATION_BUTTON))
        driver.find_element(*DoskaLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.
                                       element_to_be_clickable(DoskaLocators.LOGIN_BUTTON))
        driver.find_element(*DoskaLocators.EMAIL_INPUT).send_keys(user_login)
        driver.find_element(*DoskaLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*DoskaLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.
                                       visibility_of_element_located(DoskaLocators.USER_NAME))
        assert driver.current_url == HOME_PAGE, 'Нет перехода на главную страницу'

    def test_login_user_avatar_is_displayed(self, driver):
        user_login = generate_login_by_mask()
        fill_registration_form(driver, user_login, password)
        WebDriverWait(driver, 3).until(expected_conditions.
                                       visibility_of_element_located(DoskaLocators.USER_NAME))
        driver.find_element(*DoskaLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.
                                       element_to_be_clickable(DoskaLocators.LOGIN_AND_REGISTRATION_BUTTON))
        driver.find_element(*DoskaLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.
                                       element_to_be_clickable(DoskaLocators.LOGIN_BUTTON))
        driver.find_element(*DoskaLocators.EMAIL_INPUT).send_keys(user_login)
        driver.find_element(*DoskaLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*DoskaLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.
                                       visibility_of_element_located(DoskaLocators.USER_NAME))
        assert driver.find_element(*DoskaLocators.AVATAR).is_displayed(), 'Аватар не отображается на странице'

    def test_login_user_name_User_is_displayed(self, driver):
        user_login = generate_login_by_mask()
        fill_registration_form(driver, user_login, password)
        WebDriverWait(driver, 3).until(expected_conditions.
                                       visibility_of_element_located(DoskaLocators.USER_NAME))
        driver.find_element(*DoskaLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.
                                       element_to_be_clickable(DoskaLocators.LOGIN_AND_REGISTRATION_BUTTON))
        driver.find_element(*DoskaLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.
                                       element_to_be_clickable(DoskaLocators.LOGIN_BUTTON))
        driver.find_element(*DoskaLocators.EMAIL_INPUT).send_keys(user_login)
        driver.find_element(*DoskaLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*DoskaLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.
                                       visibility_of_element_located(DoskaLocators.USER_NAME))
        assert driver.find_element(*DoskaLocators.USER_NAME).text == DEFAULT_USER_NAME, 'Имя пользователя не User'

    def test_logout_user_login_and_registration_button_is_displayed(self, driver):
        fill_registration_form(driver, generate_login_by_mask(), password)
        WebDriverWait(driver, 3).until(expected_conditions.
                                       visibility_of_element_located(DoskaLocators.AVATAR))
        driver.find_element(*DoskaLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 3).until_not(expected_conditions.
                                           visibility_of_element_located(DoskaLocators.AVATAR and
                                                                         DoskaLocators.USER_NAME))
        assert driver.find_element(*DoskaLocators.LOGIN_AND_REGISTRATION_BUTTON).is_displayed()

