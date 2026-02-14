from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FIELD = (By.XPATH, '//*[@id="field_email"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@label="Войти"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="field_password"]')
    QR_LOGIN_BUTTON = (By.XPATH, '//button[@label="Войти по QR-коду"]')
    CANT_LOGIN_BUTTON = (By.XPATH, '//button[@aria-label="Не получается войти?"]')
    REGISTER_BUTTON = (By.XPATH, '//div[@class="LoginFormMain-module__bottom___YLtCo"]//span[@class="vkuiButton__in"]')
    LOGIN_VK = (By.XPATH, '//i[@class="i ic social-icon __s __vk_id"]')
    LOGIN_MAIL = (By.XPATH, '//i[@class="i ic social-icon __s __mailru"]')
    LOGIN_YANDEX = (By.XPATH, '//i[@class="i ic social-icon __s __yandex"]')
    BUTTON_TAB = (By.XPATH, '//a[@data-l="t,login_tab"]')
    QR_TAB = (By.XPATH, '//a[@data-l="t,qr_tab"]')
    ERROR_TEXT_LOGIN = (By.XPATH, '//span[text()="Введите логин"]')
    ERROR_TEXT_PASSWORD = (By.XPATH, '//span[text()="Введите пароль"]')

class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.QR_LOGIN_BUTTON)
        self.find_element(LoginPageLocators.CANT_LOGIN_BUTTON)
        self.find_element(LoginPageLocators.REGISTER_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_VK)
        self.find_element(LoginPageLocators.LOGIN_MAIL)
        self.find_element(LoginPageLocators.LOGIN_YANDEX)
        self.find_element(LoginPageLocators.BUTTON_TAB)
        self.find_element(LoginPageLocators.QR_TAB)

    def click_login(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    def get_error_text(self):
        return self.find_element(LoginPageLocators.ERROR_TEXT_LOGIN).text

    def input_login(self, login):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login)

    def get_error_password_text(self):
        return self.find_element(LoginPageLocators.ERROR_TEXT_PASSWORD).text