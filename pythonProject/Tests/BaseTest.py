from selenium import webdriver
import pytest


class BaseTest:
    def __init__(self):
        self.driver = webdriver.Chrome()

    @pytest.fixture
    def arrange(self):
        pass
        # тут какие то действия по подготовке окружения

    def go_to_page(self, url:str):
        self.driver.get(url)


        