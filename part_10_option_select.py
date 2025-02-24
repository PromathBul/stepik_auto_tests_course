from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

LINK = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(LINK)
    num_1 = int(browser.find_element(By.ID, 'num1').text)
    num_2 = int(browser.find_element(By.ID, 'num2').text)
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(num_1 + num_2))
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
finally:
    time.sleep(5)
    browser.quit()