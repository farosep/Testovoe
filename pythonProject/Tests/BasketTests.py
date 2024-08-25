from Pages.MainPage import MainPage
from Tests.BaseTest import BaseTest


class TestBasket(BaseTest):
    def test_basket(self):
        #Arrange
        main_page = MainPage(self.driver)

        #Act
        main_page.open_page()
        catalog_page = main_page.select_ege_11()
        catalog_page.wait_until_loaded()

        #хорошая идея будет сделать тут фиск этого косяка про фикстуры

        pass
        #Assert

