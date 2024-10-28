from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from elements.Button import Button
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.Cart import CartPage


class SharafievPage(BasePage):
    title_locator = By.XPATH, "//h1[contains(.,'Артуром Шарафиевым')]"
    in_cart_button_locator = By.CSS_SELECTOR, "[data-testid='ADD_PRODUCT_TO_CARD_BUTTON']"
    cart_locator = By.CSS_SELECTOR, "[href=\"/cart/\"]"

    def wait_until_loaded(self):
        self._wait_until_url_contains("/math-11-class-artur-sharafiev-8608")
        WebDriverWait(self.driver, 8).until(
            ec.visibility_of_element_located(self.title_locator),
            f"Элемент не отображается на странице спустя {8} секунд. Локатор: {self.title_locator}",)

    @property
    def add_to_cart_button(self):
        return Button(self.driver, self.title_locator, "Кнопка добавить в корзину")

    @property
    def go_to_cart_button(self):
        return Button(self.driver, self.cart_locator, "Кнопка перехода в корзину")

    def add_course_to_cart(self):
        self.add_to_cart_button.click()

    def go_to_cart(self):
        self.go_to_cart_button.click()
        return CartPage(self.driver)

