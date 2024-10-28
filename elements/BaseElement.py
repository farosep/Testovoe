from abc import abstractmethod

from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BaseElement:
    def __init__(self, driver: ChromeWebDriver | RemoteWebDriver, locator: [str, str], name: str = None):
        """
        :param driver: Браузер.
        :param locator: Локатор.
        :param name: Название элемента.
        """
        self._locator = locator
        self.driver = driver
        self.__name = name

    def check_visibility(self, max_timeout: int = 8):
        """ОР: Элемент отображается на странице"""
        self._find_element(max_timeout)

    @property
    @abstractmethod
    def _element(self) -> WebElement:
        """Найденный элемент с помощью одного из методов find_element"""
        pass

    def _find_element(self, max_timeout: int = 8) -> WebElement:
        """Поиск видимого элемента в DOM дереве
        Returns:
            Найденный элемент на странице
        """
        return WebDriverWait(self.driver, max_timeout).until(
            ec.visibility_of_element_located(self._locator),
            f"Элемент не отображается на странице спустя {max_timeout} секунд. Локатор: {self._locator}",
        )

    def _find_clickable_element(self, max_timeout: int = 8) -> WebElement:
        """Поиск кликабельного элемента в DOM дереве
        Returns:
            Найденный элемент на странице
        """
        return WebDriverWait(self.driver, max_timeout).until(
            ec.element_to_be_clickable(self._locator),
            f"Кликабельный элемент не отображается на странице спустя {max_timeout} секунд. Локатор: {self._locator}",
        )

    def move_to_element(self):
        """Метод предназначен для скролла до WebElement-а, если он находится за пределами видимости в окне браузера."""
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(self._element).perform()
