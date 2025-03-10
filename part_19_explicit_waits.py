from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

LINK = 'http://suninjuly.github.io/explicit_wait2.html'

browser = webdriver.Chrome()

try:
    browser.get(LINK)
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element(By.ID, 'book').click()
    value = calc(int(browser.find_element(By.ID, 'input_value').text))
    browser.find_element(By.ID, 'answer').send_keys(value)
    browser.find_element(By.ID, 'solve').click()

finally:
    time.sleep(10)
    browser.quit()