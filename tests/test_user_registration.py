from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_5.urls import HOME_PAGE
from Sprint_5.helpers import generate_login_by_mask, generate_login_not_by_mask, fill_registration_form
from Sprint_5.locators import *
from Sprint_5.data import *


class TestUserRegistration:

    def test_user_registration_new_user_go_to_home_page(self, driver):
        fill_registration_form(driver, generate_login_by_mask(), password)
        WebDriverWait(driver, 3).until(expected_conditions.
                                       visibility_of_element_located(DoskaLocators.USER_NAME))
        assert driver.current_url == HOME_PAGE, 'Нет перехода на главную страницу'

    def test_user_registration_new_user_avatar_is_displayed(self, driver):
        fill_registration_form(driver, generate_login_by_mask(), password)
        WebDriverWait(driver, 3).until(expected_conditions.
                                       visibility_of_element_located(DoskaLocators.USER_NAME))
        assert driver.find_element(*DoskaLocators.AVATAR).is_displayed(), 'Аватар не отображается на странице'

    def test_user_registration_new_user_name_User_is_displayed(self, driver):
        fill_registration_form(driver, generate_login_by_mask(), password)
        WebDriverWait(driver, 3).until(expected_conditions.
                                       visibility_of_element_located(DoskaLocators.USER_NAME))
        assert driver.find_element(*DoskaLocators.USER_NAME).text == DEFAULT_USER_NAME, 'Имя пользователя не User'

    def test_user_registration_email_not_by_mask_shows_red_color_borders(self, driver):
        fill_registration_form(driver, generate_login_not_by_mask(), password)
        WebDriverWait(driver, 3).until(expected_conditions.
                                       visibility_of_element_located(DoskaLocators.INPUT_BORDER_ERROR))
        border_property = driver.find_element(*DoskaLocators.INPUT_BORDER_ERROR).value_of_css_property('border')
        assert RED_COLOR_RGB in border_property, 'Цвет бордюра полей "Email", "Пароль", "Повторите пароль" не красный'

    def test_user_registration_email_not_by_mask_word_error_in_message(self, driver):
        fill_registration_form(driver, generate_login_not_by_mask(), password)
        WebDriverWait(driver, 3).until(expected_conditions.
                                       visibility_of_element_located(DoskaLocators.TEXT_ERROR))
        assert driver.find_element(*DoskaLocators.TEXT_ERROR).text == 'Ошибка', 'Сообщение "Ошибка" не отображается'

    def test_user_registration_an_existing_user_shows_red_color_borders(self, driver):
        user_login = generate_login_by_mask()
        fill_registration_form(driver, user_login, password)
        WebDriverWait(driver, 3).until(expected_conditions.
                                       visibility_of_element_located(DoskaLocators.USER_NAME))
        driver.find_element(*DoskaLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.
                                       element_to_be_clickable(DoskaLocators.LOGIN_AND_REGISTRATION_BUTTON))
        fill_registration_form(driver, user_login, password)
        WebDriverWait(driver, 3).until(expected_conditions.
                                       visibility_of_element_located(DoskaLocators.INPUT_BORDER_ERROR))
        border_property = driver.find_element(*DoskaLocators.INPUT_BORDER_ERROR).value_of_css_property('border')
        assert RED_COLOR_RGB in border_property, 'Цвет бордюра полей "Email", "Пароль", "Повторите пароль" не красный'

    def test_user_registration_an_existing_user_word_error_in_message(self, driver):
        user_login = generate_login_by_mask()
        fill_registration_form(driver, user_login, password)
        WebDriverWait(driver, 3).until(expected_conditions.
                                       visibility_of_element_located(DoskaLocators.USER_NAME))
        driver.find_element(*DoskaLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.
                                       element_to_be_clickable(DoskaLocators.LOGIN_AND_REGISTRATION_BUTTON))
        fill_registration_form(driver, user_login, password)
        WebDriverWait(driver, 3).until(expected_conditions.
                                       visibility_of_element_located(DoskaLocators.TEXT_ERROR))
        assert driver.find_element(*DoskaLocators.TEXT_ERROR).text == 'Ошибка', 'Сообщение "Ошибка" не отображается'
