import allure
from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.HelpPage import HelpPageHelper, HelpPageLocators
from pages.AdvertisementCabinetPage import AdvertisementCabinetHelper

BASE_URL = 'https://ok.ru/help'

@allure.suite('Проверка страницы помощи')
@allure.title('Проверка перемещения к выбранному элементу и перехода на следующую страницу')
def test_help_test(browser):
    BasePage(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelper(browser)
    HelpPage.scroll_to_item(HelpPageLocators.ADVERTISEMENT_CABINET)
    AdvertisementCabinetHelper(browser)