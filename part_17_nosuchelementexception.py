from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/wait1.html")
    # кнопки в этот момент еще нет, будет ошибка
    #time.sleep(1)
    browser.implicitly_wait(5)
    button = browser.find_element(By.ID, "verify")
    button.click()
    browser.implicitly_wait(5)
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text
finally:
    time.sleep(10)
    browser.quit()

