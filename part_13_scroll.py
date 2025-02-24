from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

LINK = 'http://suninjuly.github.io/execute_script.html'

def captcha(x):
    return str(math.log(abs(12 * math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get(LINK)
    x = int(browser.find_element(By.ID, 'input_value').text)
    res = captcha(x)
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, 'input.form-control').send_keys(res)
    browser.find_element(By.ID, 'robotCheckbox').click()
    radiobutton = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script('return arguments[0].scrollIntoView(true);', radiobutton)
    radiobutton.click()
    submit_button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    browser.execute_script('return arguments[0].scrollIntoView(true);', submit_button)
    submit_button.click()
finally:
    time.sleep(10)
    browser.quit()