from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

LINK = 'http://suninjuly.github.io/redirect_accept.html'

def capcha(x):
    return str(math.log(abs(12 * math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get(LINK)
    browser.find_element(By.CSS_SELECTOR, 'button.trollface').click()
    new_window = browser.window_handles[1] # получаем имя второй вкладки
    browser.switch_to.window(new_window)

    x = int(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.ID, 'answer').send_keys(capcha(x))
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    time.sleep(10)
    browser.quit()