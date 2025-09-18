from abc import abstractmethod
from playwright.sync_api import Page, Locator


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str = None):
        """
        :param driver: Браузер.
        :param locator: Локатор.
        :param name: Название элемента.
        """
        self._locator = locator
        self.page = page
        self.__name = name

    def check_visibility(self, max_timeout: int = 8):
        """ОР: Элемент отображается на странице"""
        self._find_element(max_timeout)


    @property
    @abstractmethod
    def _element(self) -> Locator:
        """Найденный элемент с помощью одного из методов find_element"""
        pass

    def _find_element(self, max_timeout: int = 8) -> Locator:
        """Поиск видимого элемента в DOM дереве
        Returns:
            Найденный элемент на странице
        """
        return self.page.locator(self._locator)

    def _find_clickable_element(self, max_timeout: int = 8) -> Locator:
        """Поиск кликабельного элемента в DOM дереве
        Returns:
            Найденный элемент на странице
        """
        self.page.locator(self._locator).wait_for(state="visible")
        return self.page.locator(self._locator)

    def move_to_element(self):
        """Метод предназначен для скролла до WebElement-а, если он находится за пределами видимости в окне браузера."""
        self.page.locator(self._locator).scroll_into_view_if_needed()
