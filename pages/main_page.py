from sat import *
from selenium.webdriver.common.by import By


class YandexMainPage:
    search_btn                          = Element(By.CSS_SELECTOR, '.suggest2-form__button', 'Найти')
    empty_desc_elm                      = Element(By.CSS_SELECTOR, '.content__left .misspell__message', 'Результат пустого запроса')


