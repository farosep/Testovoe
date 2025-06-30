from selenium.webdriver.common.by import By

from elements.Button import Button
from pages.BasePage import BasePage

from elements.BaseElement import BaseElement
from pages.SharafievPage import SharafievPage


class MathCatalogPage(BasePage):

    _page_title_selector =  "//h1[contains(., 'Математике')]"
    _profile_math_sharafiev_locator = "[data-testid='PRODUCT_CARD'] a[href='/ege/math-11-class-artur-sharafiev-8608/']"

    def wait_until_loaded(self):
        self._wait_until_url_contains("11-class/math/")
        self.title().check_visibility()

    def title(self):
        return BaseElement(self.page, self._page_title_selector, "Заголовок страницы Подготовка к ЕГЭ по Математике")

    @property
    def button_sharafiev_cource(self):
        return Button(self.page, self._profile_math_sharafiev_locator, "Кнопка добавления курса Шарафиева в корзину")

    def select_sharafiev_course(self):
        self.button_sharafiev_cource.click()
        return SharafievPage(self.page)



