from selenium import webdriver
from selenium.webdriver.common.by import By

LINK = 'http://selenium1py.pythonanywhere.com/'

class TestMainPage1():
    @classmethod
    def setup_class(cls):
        print('\nstart browser for test suite...')
        cls.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(cls):
        print('\nquit browser for test suite ...')
        cls.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(LINK)
        self.browser.find_element(By.CSS_SELECTOR, '#login_link')

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(LINK)
        self.browser.find_element(By.CSS_SELECTOR, '.basket-mini .btn-group > a')

class TestMainPage2():
    def setup_method(self):
        print('start browser for test...')
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print('start browser for test...')
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(LINK)
        self.browser.find_element(By.CSS_SELECTOR, '#login_link')

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(LINK)
        self.browser.find_element(By.CSS_SELECTOR, '.basket-mini .btn-group > a')
