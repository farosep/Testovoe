from Pages.MainPage import MainPage
from Tests.BaseTest import BaseTest


class BasketTest(BaseTest):
    def basket_test(self):
        #Arrange
        main_page = MainPage(self.driver)

        #Act
        main_page.open_page()
        catalog_page = main_page.select_ege_11()
        catalog_page.wait_until_loaded()



        #Assert

