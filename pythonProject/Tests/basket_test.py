from pages.MainPage import MainPage
from tests.base_test import BaseTest


class TestBasket(BaseTest):
    def test_basket(self):
        #Arrange
        main_page = MainPage(self.driver)

        #Act
        main_page.open_page()
        main_page.select_parents_radio()
        catalog_page = main_page.select_11_class() # не не может выполниться
        catalog_page.wait_until_loaded()
        catalog_page.select_profil_math()
        course_page = catalog_page.select_sharafiev_course()
        course_page.wait_until_loaded()
        course_page.add_course_to_basket() # Не отрабатывает
        basket_page = course_page.go_to_basket()

        # Assert
        basket_page.check_product_is_added() # продукт не добавился, а проверка прошла


