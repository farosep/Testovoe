

from elements.BaseElement import BaseElement
from elements.Button import Button
from pages.BasePage import BasePage
from pages.Catalog import CatalogPage


class MainPage(BasePage):
    _page_url = "https://umschool.net/"

    _name_input = "[data-testid='INPUT_FIELD_full_name']"

    _parent_radio_selector = "[data-testid='TAB_parent']"
    _student_radio_selector = "[data-testid='TAB_child']"
    _cart_button_selector =  "[data-testid='HEADER_CART_BUTTON']"

    _select_ege = "(//a[@href='/ege/'])[2]"

    @property
    def button_cart(self):
        return Button(self.page, self._cart_button_selector, "Кнопка для перехода в корзину")

    @property
    def button_parent(self):
        return Button(self.page, self._parent_radio_selector, "Кнопка фильтра для родителей")

    @property
    def button_ege(self):
        return Button(self.page, self._select_ege, "кнопка фильтра егэ")

    def open_page(self):
        self.page.goto(self._page_url)
        self.wait_until_loaded()
        return self

    def wait_until_loaded(self):
        self._wait_until_url_contains("/umschool.net")
        BaseElement(
            self.page, self._name_input, "Проверяем появилось ли поле для ввода данных"
        ).check_visibility()

    def select_parents_radio(self):
        self.button_parent.click()
        return self

    def go_to_ege_catalog_page(self):
        self.button_ege.click()
        return CatalogPage(self.page)





