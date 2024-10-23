from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from elements.BaseElement import BaseElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasketPage(BasePage):
    title_locator = By.CSS_SELECTOR, "#__nuxt > main > div.mx-auto.w-\[1446px\].max-w-full.p-container > div.my-8.sm\:my-10.text-center > h1"
    product_wiget_locator = By.XPATH, '//*[@id="__nuxt"]/main/div[2]/div[2]/section[1]/div[2]'

    def wait_until_loaded(self):
        self._wait_until_url_contains("/cart")
        WebDriverWait(self.driver, 8).until(
            ec.visibility_of_element_located(self.title_locator),
            f"Элемент не отображается на странице спустя {8} секунд. Локатор: {self.title_locator}",)

    @property
    def product_wiget(self):
        return BaseElement(self.driver, self.product_wiget_locator, "Виджет товара")

    def check_product_is_added(self):
        return self.product_wiget
