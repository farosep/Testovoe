
from pages.SharafievPage import SharafievPage
from elements.Button import Button
from pages.BasePage import BasePage
from pages.MathCatalogPage import MathCatalogPage


class CatalogPage(BasePage):
    base_math_selector = "[data-scroll-item=\"3\"]"
    select_subject_selector = "//button[@data-testid='FILTER_CLASS_TYPES_BUTTON']"
    russian_selector = "//*[@data-testid='FILTER_CLASS_TYPE_ITEM']//span[text()='Русский язык']"
    math_selector = "//*[@data-testid='FILTER_CLASS_TYPE_ITEM']//span[text()='Математика']"
    all_subjects_selector = "#__nuxt > main > div > div.ui-radius-md.ums-card.ums-component-root.ui-bg-grey-0.ui-px-3.ui-py-4.sm\:ui-p-4.md\:ui-p-5.lg\:ui-p-8.space-y-8.sm\:space-y-10.lg\:space-y-20.my-8.md\:my-20 > div > div.mb-9.sm\:mb-10.md\:mb-14.lg\:mb-20 > div > div.base-slider.base-slider--with-offset.base-slider--full-height > div.base-slider__area.no-scrollbar > div:nth-child(1)"
    profile_math_sharafiev_locator = "//a[@href='/ege/math-11-class-artur-sharafiev-10694/']"
    slide_over_apply_locator = "//*[@data-testid='SLIDE_OVER_APPLY_BUTTON']"

    def wait_until_loaded(self):
        self._wait_until_url_contains("/ege/")

    def select_profil_math(self):
        self.button_select_subject.click()
        self.button_math_subject.click()
        self.button_apply_filters.click()
        return self

    def select_sharafiev_course(self):
        self.button_sharafiev_cource.click()
        return SharafievPage(self.page)

    @property
    def button_base_math(self):
        return Button(self.page, self.base_math_selector, "Кнопка базовой математики")

    @property
    def button_select_subject(self):
        return Button(self.page, self.select_subject_selector, "Кнопка вызова меню выбора предметов")

    @property
    def button_math_subject(self):
        return Button(self.page, self.math_selector, "Кнопка выбора профильной математики")

    @property
    def button_apply_filters(self):
        return Button(self.page, self.slide_over_apply_locator, "Кнопка Применить фильтры по курсам")

    @property
    def button_sharafiev_cource(self):
        return Button(self.page, self.profile_math_sharafiev_locator, "Кнопка добавления курса Шарафиева в корзину")