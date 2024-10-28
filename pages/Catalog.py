from selenium.webdriver.common.by import By
from pages.SharafievPage import SharafievPage
from elements.Button import Button
from pages.BasePage import BasePage
from pages.MathCatalogPage import MathCatalogPage


class CatalogPage(BasePage):
    base_math_selector = By.CSS_SELECTOR, "[data-scroll-item=\"3\"]"
    profile_math_selector = By.CSS_SELECTOR, "div.mb-9.sm\\:mb-10.md\\:mb-14.lg\\:mb-20 > div > div.base-slider.base-slider--with-offset.base-slider--full-height > div.base-slider__area.no-scrollbar > div:nth-child(3) > div"
    russian_selector = By.CSS_SELECTOR, "[data-scroll-item=\"1\"]"
    all_subjects_selector = By.CSS_SELECTOR, "#__nuxt > main > div > div.ui-radius-md.ums-card.ums-component-root.ui-bg-grey-0.ui-px-3.ui-py-4.sm\:ui-p-4.md\:ui-p-5.lg\:ui-p-8.space-y-8.sm\:space-y-10.lg\:space-y-20.my-8.md\:my-20 > div > div.mb-9.sm\:mb-10.md\:mb-14.lg\:mb-20 > div > div.base-slider.base-slider--with-offset.base-slider--full-height > div.base-slider__area.no-scrollbar > div:nth-child(1)"
    profile_math_sharafiev_locator = By.CSS_SELECTOR, "[data-testid=\"PRODUCT_CARD\"] a[href=\"/ege/math-11-class-artur-sharafiev-8608/\"]"

    def wait_until_loaded(self):
        self._wait_until_url_contains("/11-class")

    def select_profil_math(self):
        self.button_profile_math.click()
        return MathCatalogPage(self.driver)

    def select_sharafiev_course(self):
        self.button_sharafiev_cource.click()
        return SharafievPage(self.driver)

    @property
    def button_base_math(self):
        return Button(self.driver, self.base_math_selector, "Кнопка базовой математики")

    @property
    def button_profile_math(self):
        return Button(self.driver, self.profile_math_selector, "Кнопка профильной математики")

    @property
    def button_sharafiev_cource(self):
        return Button(self.driver, self.profile_math_sharafiev_locator, "Кнопка добавления курса Шарафиева в корзину")