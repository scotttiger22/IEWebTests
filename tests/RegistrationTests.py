import allure
from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
from pages.RegistrationPage import RegistrationPageHelper


BASE_URL = 'https://ok.ru/'
REGISTRATION_URL = 'https://id.vk.com/auth?app_id=7525058&response_type=silent_token&lang_id=0&v=1.61.2&redirect_uri=https%3A%2F%2Fok.ru&client_metadata=eyJ2ZHQiOm51bGwsInVzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTQ1LjAuMC4wIFNhZmFyaS81MzcuMzYiLCJzdGF0X2lkIjoiYWVhZTc1MjgtZGFmOS00MzliLWJlOWMtMzk0ZGE5ZGJjODBmIiwid2ViX2RvbWFpbiI6InJ1IiwianNfZW5hYmxlZCI6dHJ1ZSwic2NyZWVuX3NpemUiOm51bGwsImJyb3dzZXJfc2l6ZSI6bnVsbCwiYnJvd3Nlcl9jb29raWVJZCI6IjU3MjAxMTIxNzUzNTAzMzMyMzgiLCJyZWZlcmVyX3VybCI6bnVsbCwiYXBwX3RhZyI6bnVsbCwibXlfdHJhY2tlcl9pZCI6Ijg3NjYzNTY3IiwibG9naW5faW50ZW50X3Rva2VuIjpudWxsLCJ2ZXJpZmljYXRpb25fc3VwcG9ydGVkX3YiOm51bGx9&scheme=light'

@allure.suite('Проверка формы авторизации')
@allure.title('Проверка ошибки при пустой форме авторизации')
def test_registration_random_country(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    BasePage(browser).get_url(REGISTRATION_URL)
    RegistrationPage = RegistrationPageHelper(browser)
    Selected_country_code = RegistrationPage.select_random_country()
    Actual_country_code = RegistrationPage.get_phone_field_value()
    assert Selected_country_code == Actual_country_code