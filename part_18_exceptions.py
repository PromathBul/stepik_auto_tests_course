from selenium import webdriver
from selenium.webdriver.common.by import By

LINK = 'http://suninjuly.github.io/cats.html'

browser = webdriver.Chrome()

try:
    browser.get(LINK)
    browser.find_element(By.ID, 'button')

finally:
    browser.quit()