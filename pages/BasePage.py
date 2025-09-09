from abc import abstractmethod
import re
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        """
        :param page: Страница для взаимодействия с браузером.
        """
        self.page = page

    def _wait_until_url_contains(self, url: str, max_timeout: int = 8000):
        """
        Ожидание появления в URL заданного значения.

        :param url: Значение, которое ожидается в URL.
        :param max_timeout: Максимальное время ожидания в секундах.
        """
        self.page.wait_for_url(re.compile(rf"{url}"), timeout=max_timeout)

    def refresh(self):
        """Метод для перезагрузки страницы браузера"""
        try:
            self.page.reload()
        except TimeoutError:
            self.page.evaluate("window.stop();")

    @abstractmethod
    def wait_until_loaded(self):
        """
        Абстрактный метод для ожидания загрузки компонента.
        """
        pass
