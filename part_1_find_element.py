from selenium import webdriver
from selenium.webdriver.common.by import By # содержит локаторы для поиска
import time

# открытие браузера
browser = webdriver.Chrome()
# заходим на сайт
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
time.sleep(5)
# получаем веб-элемент c id 'submit_button'
button = browser.find_element(By.ID, 'submit_button')
print(button.size)

# завершение процесса работы c браузером
browser.quit()