from selenium import webdriver


class BaseTest:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def go_to_page(self, url:str):
        self.driver.get(url)