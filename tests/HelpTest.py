import allure
from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.HelpPage import HelpPageHelperHelper, HelpPageLocators
from pages.AdvertisementCabinetPage import AdvertisementCabinetHelper

BASE_URL = 'https://ok.ru/help'

@allure.suite('Проверка страницы помощи')
@allure.title('Проверка перемещения к выбранному элементу и перехода на следующую страницу')
def test_help_test(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelperHelper(browser)
    HelpPage.scroll_to_item(HelpPageLocators.ADVERTISEMENT_CABINET)
    AdvertisementCabinetHelper(browser)