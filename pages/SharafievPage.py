from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from elements.Button import Button
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.Cart import CartPage


class SharafievPage(BasePage):
    title_locator =  "//h1[contains(.,'Артуром Шарафиевым')]"
    in_cart_button_locator =  "[data-testid='ADD_PRODUCT_TO_CARD_BUTTON']"
    cart_locator =  "[href=\"/cart/\"]"

    def wait_until_loaded(self):
        self._wait_until_url_contains("/math-11-class-artur-sharafiev-8608")
        self.page.locator(self.title_locator).wait_for(state="visible")

    @property
    def add_to_cart_button(self):
        return Button(self.page, self.title_locator, "Кнопка добавить в корзину")

    @property
    def go_to_cart_button(self):
        return Button(self.page, self.cart_locator, "Кнопка перехода в корзину")

    def add_course_to_cart(self):
        self.add_to_cart_button.click()

    def go_to_cart(self):
        self.go_to_cart_button.click()
        return CartPage(self.page)

