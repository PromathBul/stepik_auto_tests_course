from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

LINK = 'http://suninjuly.github.io/file_input.html'

data =[('firstname', 'Dmitrii'), ('lastname', 'Tikhonov'), ('email', 'qwerty@gmail.com')]

try:
    browser = webdriver.Chrome()
    browser.get(LINK)
    for info in data:
        browser.find_element(By.NAME, info[0]).send_keys(info[1])

    filepath = os.path.abspath(os.path.dirname(__file__))

    browser.find_element(By.ID, 'file').send_keys(filepath)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
finally:
    time.sleep(10)
    browser.quit()