from unittest2 import *
from sat import *
from pages.main_page import MainPage


class TestMainPage(TestCase):
    main_page = MainPage()

    def setUp(self) -> None:
        log('Открываем главную страницу яндекса')
        Browser('https://yandex.ru/')

    def test_01_man_page(self):
        log('Проверяем кнопку "найти"')
        self.main_page.search_btn.should_be(Displayed)
        self.main_page.search_btn.click()
        delay(5)

    def tearDown(self) -> None:
        close_window()


if __name__ == '__main__':
    main()
