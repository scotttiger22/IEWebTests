import pytest
from selenium  import webdriver

@pytest.fixture(scope='session')
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-cache")
    driver = webdriver.Chrome(options=options)
    driver.delete_all_cookies()
    yield driver
    driver.quit()
