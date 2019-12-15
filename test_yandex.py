from unittest2 import *
from sat import *
from pages.main_page import YandexMainPage


class TestMainPage(TestCase):
    main_page = YandexMainPage()

    def setUp(self) -> None:
        log('Открываем главную страницу яндекса')
        Browser('https://yandex.ru/')

    def test_01_man_page(self):
        log('Проверяем кнопку "найти"')
        self.main_page.search_btn.should_be(Displayed).click()
        self.main_page.empty_desc_elm.should_be(Displayed, wait_time=20).click()
        delay(5)

    def tearDown(self) -> None:
        close_window()


if __name__ == '__main__':
    main()
