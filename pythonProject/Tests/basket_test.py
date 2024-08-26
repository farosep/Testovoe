from pages.MainPage import MainPage
from tests.base_test import BaseTest


class TestBasket(BaseTest):
    def test_basket(self):
        #Arrange
        main_page = MainPage(self.driver)

        #Act
        main_page.open_page()
        main_page.select_parents_radio()
        catalog_page = main_page.select_11_class()
        catalog_page.wait_until_loaded()
        catalog_page.button_profile_math.scroll_to_element()
        catalog_page.select_profil_math()
        catalog_page.select_sharafiev_course()


        pass
        #Assert

