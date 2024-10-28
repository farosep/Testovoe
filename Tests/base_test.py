from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
import pytest


class BaseTest:
    driver: ChromeWebDriver | RemoteWebDriver

    @pytest.fixture(autouse=True)
    def setup(self, create_local):
        self.driver = create_local



