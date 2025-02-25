import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

link_1 = "http://suninjuly.github.io/registration1.html"
link_2 = "http://suninjuly.github.io/registration2.html"

def main_script(link):
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_classes = ['first', 'second', 'third']
    for i in range(len(input_classes)):
        input = browser.find_element(By.CSS_SELECTOR, f'.first_block .{input_classes[i]}')
        input.send_keys('*')

    # Отправляем заполненную форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    browser.implicitly_wait(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt, который хранится в свойстве text
    return welcome_text_elt.text
class TestRegistration(unittest.TestCase):
    def test_first_link(self):
        welcome_text = main_script(link_1)
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Регистрация не прошла")

    def test_second_link(self):
        welcome_text = main_script(link_2)
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Регистрация не прошла")

if __name__ == "__main__":
    unittest.main()