from selenium.webdriver.common.by import By

from elements.BaseElement import BaseElement
from elements.Button import Button
from pages.BasePage import BasePage
from pages.Catalog import Catalog


class MainPage(BasePage):
    page_url = "https://umschool.net/"

    name_input = By.CSS_SELECTOR, "[data-testid=\"INPUT_FIELD_full_name\"]"

    parent_radio_selector = By.CSS_SELECTOR, "[data-testid=\"TAB_parent\"]"
    student_radio_selector = By.CSS_SELECTOR, "[data-testid=\"TAB_child\"]"

    select_ege_11_selector = By.CSS_SELECTOR, "div > a[href=\"/ege/11-class/\"]"
    select_ege_10_selector = By.CSS_SELECTOR, "div > a[href=\"/ege/11-class/\"]"
    select_oge_9_selector = By.CSS_SELECTOR, "div > a[href=\"/ege/11-class/\"]"

    @property
    def button_student(self):
        return Button(self.driver, self.parent_radio_selector, "Указываем что мы Родитель")

    def open_page(self):
        self.driver.get(self.page_url)
        return self

    def wait_until_loaded(self):
        self._wait_until_url_contains("/oauth")
        BaseElement(
            self.driver, self.name_input, "Проверяем появилось ли поле для ввода данных"
        ).check_visibility()

    def select_ege_11(self):
        #Тут нужно ожидание
        self.button_student.click()
        return Catalog(self.driver)





