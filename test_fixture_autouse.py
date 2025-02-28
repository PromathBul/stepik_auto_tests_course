import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

LINK = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture
def browser():
    print('\nstart browser for test ...')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser ...')
    browser.quit()

# запускается для каждого теста без явного вызова и передачи
@pytest.fixture(autouse=True)
def prepare_data():
    print('\npreparing some critical data for every test')

class TestMainPage:
    def test_guest_should_see_login_link(self, browser):
        browser.get(LINK)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(LINK)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")