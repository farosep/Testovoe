
import pytest
from playwright.sync_api import Page


class BaseTest:
    driver: Page

    @pytest.fixture(autouse=True)
    def setup(self, create_local):
        self.page = create_local



