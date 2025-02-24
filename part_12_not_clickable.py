from selenium import webdriver
from selenium.webdriver.common.by import By
import time

LINK = 'https://suninjuly.github.io/execute_script.html'

try:
    browser = webdriver.Chrome()
    browser.get(LINK)
    # будет ошибка, так как футер перекрывает кнопку, если не проскроллить
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    time.sleep(1)
    #прокручиваем экран, чтобы кнопка была в поле видимости (аргумент true)
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # прокрутить экран на определенное количество пикселей, например, на 100
    # browser.execute_script("window.scrollBy(0, 100);")
    time.sleep(1)
    button.click()
finally:
    time.sleep(5)
    browser.quit()