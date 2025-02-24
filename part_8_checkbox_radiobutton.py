from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

LINK = "https://suninjuly.github.io/math.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(LINK)

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    radiobutton.click()

    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()
finally:
    time.sleep(30)
    browser.quit()
