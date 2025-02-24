from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

LINK = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(LINK)

    chest = browser.find_element(By.ID, 'treasure')
    x = chest.get_attribute('valuex')
    y = calc(x)
    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)

    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()

    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()
finally:
    time.sleep(10)
    browser.quit()