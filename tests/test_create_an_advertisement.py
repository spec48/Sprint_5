from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_5.urls import PROFILE_PAGE
from Sprint_5.helpers import generate_login_by_mask, fill_registration_form
from Sprint_5.locators import *
from Sprint_5.data import *


class TestCreateAdvertisement:

    def test_create_advertisement_unauthorized_user_window_title_is_displayed(self, driver):
        driver.find_element(*DoskaLocators.POST_AD_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.
                                       visibility_of_element_located(DoskaLocators.POST_AD_FORM))
        assert driver.find_element(*DoskaLocators.POST_AD_TEXT).text == 'Чтобы разместить объявление, авторизуйтесь',\
            'Заголовок не соответствует "Чтобы разместить объявление, авторизуйтесь"'

    def test_create_advertisement_authorized_user_advertisement_is_displayed(self, driver):
        fill_registration_form(driver, generate_login_by_mask(), password)
        WebDriverWait(driver, 3).until(expected_conditions.
                                       visibility_of_element_located(DoskaLocators.USER_NAME))
        driver.find_element(*DoskaLocators.POST_AD_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.
                                       element_to_be_clickable(DoskaLocators.PUBLISH_BUTTON))
        driver.find_element(*DoskaLocators.PRODUCT_NAME_INPUT).send_keys(product_name)
        driver.find_element(*DoskaLocators.PRODUCT_DESCRIPTION_TEXTAREA).send_keys(product_description)
        driver.find_element(*DoskaLocators.PRODUCT_PRICE_INPUT).send_keys(product_price)
        driver.find_element(*DoskaLocators.CATEGORY_DROPDOWN).click()
        driver.find_element(*DoskaLocators.BOOKS_BUTTON_FROM_CATEGORY).click()
        driver.find_element(*DoskaLocators.CITY_DROPDOWN).click()
        driver.find_element(*DoskaLocators.N_NOVGOROD_BUTTON_FROM_CITY).click()
        driver.find_element(*DoskaLocators.RADIO_BUTTON).click()
        driver.find_element(*DoskaLocators.PUBLISH_BUTTON).click()
        driver.get(PROFILE_PAGE)
        WebDriverWait(driver, 3).until(expected_conditions.
                                       visibility_of_element_located(DoskaLocators.CARD_EXIST))
        card = driver.find_element(*DoskaLocators.CARD_EXIST)
        driver.execute_script("arguments[0].scrollIntoView();", card)
        assert driver.find_element(*DoskaLocators.CARD_EXIST).is_displayed()
