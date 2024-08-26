from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.common.exceptions import TimeoutException
from abc import abstractmethod
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver: ChromeWebDriver | RemoteWebDriver):
        """
        :param driver: Веб-драйвер для взаимодействия с браузером.
        """
        self.driver = driver

    def _wait_until_url_contains(self, url: str, max_timeout: int = 8):
        """
        Ожидание появления в URL заданного значения.

        :param url: Значение, которое ожидается в URL.
        :param max_timeout: Максимальное время ожидания в секундах.
        """
        WebDriverWait(self.driver, max_timeout).until(ec.url_contains(url), f"В URL нет ожидаемого значения '{url}'")

    def refresh(self):
        """Метод для перезагрузки страницы браузера"""
        try:
            self.driver.refresh()
        except TimeoutException:
            self.driver.execute_script("window.stop();")

    @abstractmethod
    def wait_until_loaded(self):
        """
        Абстрактный метод для ожидания загрузки компонента.
        """
        pass
