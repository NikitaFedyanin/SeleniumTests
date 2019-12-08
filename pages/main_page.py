from sat import *
from selenium.webdriver.common.by import By


class MainPage:
    search_btn                          = Element(By.CSS_SELECTOR, '.suggest2-form__button', 'Найти')


    def search_click(self):
        self.search_btn.click()
