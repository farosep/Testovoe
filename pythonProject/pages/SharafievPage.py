from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from elements.Button import Button
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.Basket import BasketPage


class SharafievPage(BasePage):
    title_locator = By.CSS_SELECTOR, "#__nuxt > main > div:nth-child(1) > div.my-8.sm\\:my-10.text-center > h1"
    in_basket_button_locator = By.CSS_SELECTOR, "#__nuxt > main > div:nth-child(1) > div:nth-child(2) > div > div.p-4.sm\:p-5.md\:p-8.space-y-8 > div.flex.justify-start.flex-wrap.gap-4.flex-col-reverse.sm\:flex-row > button"
    basket_locator = By.CSS_SELECTOR, "[href=\"/cart/\"]"

    def wait_until_loaded(self):
        self._wait_until_url_contains("/math-11-class-artur-sharafiev-8608")
        WebDriverWait(self.driver, 8).until(
            ec.visibility_of_element_located(self.title_locator),
            f"Элемент не отображается на странице спустя {8} секунд. Локатор: {self.title_locator}",)

    @property
    def add_to_basket_button(self):
        return Button(self.driver, self.title_locator, "Кнопка добавить в корзину")

    @property
    def go_to_basket_button(self):
        return Button(self.driver, self.basket_locator, "Кнопка перехода в корзину")

    def add_course_to_basket(self):
        self.add_to_basket_button.click()

    def go_to_basket(self):
        self.go_to_basket_button.click()
        return BasketPage(self.driver)

