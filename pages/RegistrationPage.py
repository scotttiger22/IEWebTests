from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure
import random

class RegistrationPageLocators:
    PHONE_FIELD = (By.XPATH, '//input[@name="phone"]')
    COUNTRY_LIST = (By.XPATH, '//span[@class="vkuiFormField__before"]')
    COUNTRY_ITEM = (By.XPATH,'//div[@class="CountryList-module_countryList__listItemCode__LzHon"]//span[@class="vkuiText__host vkuiText__sizeYNone vkuiTypography__host vkuiTypography__normalize vkuiRootComponent__host"]')
    SUBMIT_BUTTON = (By.XPATH, '//span[text()="Далее"]')

class RegistrationPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        # self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.find_element(RegistrationPageLocators.PHONE_FIELD)
            self.find_element(RegistrationPageLocators.COUNTRY_LIST)
            self.find_element(RegistrationPageLocators.COUNTRY_ITEM)
            self.find_element(RegistrationPageLocators.SUBMIT_BUTTON)

    @allure.step('Выбираем рандомную страну')
    def select_random_country(self):
        self.attach_screenshot()
        random_number = random.randint(0, 205)
        self.find_element(RegistrationPageLocators.COUNTRY_LIST).click()
        country_items = self.find_elements(RegistrationPageLocators.COUNTRY_ITEM)
        country_code = country_items[random_number].text
        country_items[random_number].click()
        return country_code

    @allure.step('Получаем код выбранной страны, отображенный в поле вода телефона')
    def get_phone_field_value(self):
        a = self.find_element(RegistrationPageLocators.PHONE_FIELD).get_attribute('value')
        return a.strip()

