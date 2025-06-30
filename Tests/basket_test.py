from pages.MainPage import MainPage
from Tests.base_test import BaseTest


class TestBasket(BaseTest):

    # TODO починить выпавшие ошибки

    def test_cart(self):
        #Arrange
        main_page = MainPage(self.page)

        #Act
        main_page.open_page()
        main_page.select_parents_radio()
        catalog_page = main_page.go_to_ege_catalog_page()
        catalog_page.wait_until_loaded()
        math_catalog_page = catalog_page.select_profil_math()
        course_page = math_catalog_page.select_sharafiev_course()
        course_page.wait_until_loaded()
        course_page.add_course_to_cart()
        basket_page = course_page.go_to_cart()

        # Assert
        basket_page.check_product_is_added()


