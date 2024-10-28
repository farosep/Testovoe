from pages.MainPage import MainPage
from Tests.base_test import BaseTest


class TestBasket(BaseTest):

    # TODO 1)

    def test_cart(self):
        #Arrange
        main_page = MainPage(self.driver)

        #Act
        main_page.open_page()
        main_page.select_parents_radio() # Тут ElementClickInterceptedException
        catalog_page = main_page.select_11_class() # StaleElementReferenceException падает но очень редко
        catalog_page.wait_until_loaded()
        math_catalog_page = catalog_page.select_profil_math()
        course_page = math_catalog_page.select_sharafiev_course() # StaleElementReferenceException падает часто
        course_page.wait_until_loaded()
        course_page.add_course_to_cart() # Тут почему то не роисходит добавление в корзину
        basket_page = course_page.go_to_cart()

        # Assert
        basket_page.check_product_is_added()


