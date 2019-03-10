import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

SELENIUM_TIMEOUT = 10


class TestPageAuthorization(unittest.TestCase):
    LOGINN = 'test.qatest2@yandex.ru'
    PASSWORD = 'z34WJCB11'
    URL_ADDRESS_SITE = 'https://passport.yandex.ru/auth/list?retpath=https%3A%2F%2Fpassport.yandex.ru%2Fprofile&noreturn=1'
    browser = None

    # Переход на страницу яндекс с выбором почты
    def setUp(self):
        self.browser = webdriver.Chrome()
        # Открытие окна браузера на максимальном разрешении
        self.browser.maximize_window()
        self.browser.get(self.URL_ADDRESS_SITE)

    # Закрытие браузера после выполнение теста
    def tearDown(self):
        self.browser.close()

    def test_log(self):
        time.sleep(1)
        # Поиск поля ввода логина почты
        find_input_logo = self.browser.find_element(By.XPATH, "//div//input[@id = 'passp-field-login']")
        # Ввод адреса почты
        find_input_logo.send_keys(self.LOGINN)
        # Поиск кнопки "Войти"
        button_sign_in = self.browser.find_element(By.CSS_SELECTOR, '.passp-sign-in-button button')
        # Поиск название кнопки
        button_sign_in_text = button_sign_in.find_element(By.CSS_SELECTOR, '.button2__text')
        # Проверка название кнопки "Войти"
        assert ('Войти' == button_sign_in_text.text), 'Error name button'
        # Клик по кнопки 
        button_sign_in.click()
        time.sleep(1)
        # Поиск поля "Введите пароль"
        find_input_pass = self.browser.find_element(By.XPATH, "//div//input[@id = 'passp-field-passwd']")
        # Ввести пароль в поле
        find_input_pass.send_keys(self.PASSWORD)
        # Поиск кнопки войти
        button_sign_in = self.browser.find_element(By.CSS_SELECTOR, '.passp-sign-in-button button')
        # Поиск название кнопки
        button_sign_in_text = button_sign_in.find_element(By.CSS_SELECTOR, '.button2__text')
        # Проверка название кнопки "Войти"
        assert ('Войти' == button_sign_in_text.text), 'Error name button'
        # Клик по кнопки
        button_sign_in.click()
        time.sleep(2)
        # Поиск текста "Неверный пароль"
        no_log = self.browser.find_element(By.CSS_SELECTOR, '.passp-form-field .passp-form-field__error')
        assert('Неверный пароль' == no_log.text), 'Error text form pass error'
        
if __name__ == '__main__':
    unittest.main()

