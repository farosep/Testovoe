from selenium.webdriver.common.by import By

from elements.BaseElement import BaseElement
from elements.Button import Button
from pages.BasePage import BasePage
from pages.Catalog import CatalogPage


class MainPage(BasePage):
    _page_url = "https://umschool.net/"

    _name_input = By.CSS_SELECTOR, "[data-testid='INPUT_FIELD_full_name']"

    _parent_radio_selector = By.CSS_SELECTOR, "[data-testid='TAB_parent']"
    _student_radio_selector = By.CSS_SELECTOR, "[data-testid='TAB_child']"
    _cart_button_selector = By.CSS_SELECTOR, "[data-testid='HEADER_CART_BUTTON']"

    _select_ege_11_selector = By.CSS_SELECTOR, "div > a[href='/ege/11-class/']"
    _select_ege_10_selector = By.CSS_SELECTOR, "div > a[href='/ege/11-class/']"
    _select_oge_9_selector = By.CSS_SELECTOR, "div > a[href='/ege/11-class/']"

    @property
    def button_cart(self):
        return Button(self.driver, self._cart_button_selector, "Кнопка для перехода в корзину")

    @property
    def button_parent(self):
        return Button(self.driver, self._parent_radio_selector, "Кнопка фильтра для родителей")

    @property
    def button_ege_11(self):
        return Button(self.driver, self._select_ege_11_selector, "кнопка фильтра егэ 11 класса")

    def open_page(self):
        self.driver.get(self._page_url)
        self.wait_until_loaded()
        return self

    def wait_until_loaded(self):
        self._wait_until_url_contains("/umschool.net")
        BaseElement(
            self.driver, self._name_input, "Проверяем появилось ли поле для ввода данных"
        ).check_visibility()

    def select_parents_radio(self):
        self.button_parent.click()
        return self

    def select_11_class(self):
        self.button_ege_11.click()
        return CatalogPage(self.driver)





