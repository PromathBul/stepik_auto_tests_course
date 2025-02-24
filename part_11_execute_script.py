from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.execute_script('document.title = "execute_script";')
    browser.execute_script('alert("Hello, world!");')
finally:
    time.sleep(10)
    browser.quit()