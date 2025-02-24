from selenium import webdriver
from selenium.webdriver.common.by import By
import time

LINK = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(LINK)
    time.sleep(3)
    button = browser.find_element(By.ID, "submit_button")
    # эмулирование нажатия на кнопку
    button.click()
    time.sleep(3)
# выполнится даже, если скрипт упадет c ошибкой
finally:
    browser.quit()