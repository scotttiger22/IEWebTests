import pytest
from selenium  import webdriver

@pytest.fixture(scope='session')
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-cache")
    options.add_argument("--lang=ru")
    driver = webdriver.Remote(command_executor ="159.194.203.73:4444", options=options)
    driver.delete_all_cookies()
    yield driver
    if driver:
        driver.quit()
