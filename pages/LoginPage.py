from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FIELD = (By.XPATH, '//*[@id="field_email"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@label="Войти"]')
    PASSWORD_BUTTON = (By.XPATH, '//*[@id="field_password"]')
    QR_LOGIN_BUTTON = (By.XPATH, '//button[@label="Войти по QR-коду"]')
    CANT_LOGIN_BUTTON = (By.XPATH, '//button[@aria-label="Не получается войти?"]')
    REGISTER_BUTTON = (By.XPATH, '//button[@class="vkuiInternalTappable vkuiButton__host vkuiButton__sizeL vkuiButton__modeSecondary vkuiButton__appearanceNeutral vkuiButton__sizeYNone vkuiButton__stretched vkuiTappable__host vkuiTappable__sizeXNone vkuiTappable__hasPointerNone vkuiClickable__host vkuiClickable__realClickable vkuistyles__-focus-visible vkuiRootComponent__host"]')
    LOGIN_VK = (By.XPATH, '//i[@class="i ic social-icon __s __vk_id"]')
    LOGIN_MAIL = (By.XPATH, '//i[@class="i ic social-icon __s __mailru"]')
    LOGIN_YANDEX = (By.XPATH, '//i[@class="i ic social-icon __s __yandex"]')
    BUTTON_LOGIN = (By.XPATH, '//a[@id="login-7548991407"]')
    QR_BUTTON = (By.XPATH, '//a[@id="qrCode-7548991471"]')

class LoginPageHelper(BasePage):
    pass

