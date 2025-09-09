from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from elements.BaseElement import BaseElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class CartPage(BasePage):
    product_wiget_locator = '[data-testid="CART_ITEM"]'

    def wait_until_loaded(self):
        self._wait_until_url_contains("/cart")

    @property
    def product_wiget(self):
        return BaseElement(self.page, self.product_wiget_locator, "Виджет товара")

    def check_product_is_added(self):
        return self.product_wiget.check_visibility()
