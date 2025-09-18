import pytest
import datetime
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def create_remote():
    browser = sync_playwright().start().chromium.connect_over_cdp(
        "какой то url для коннекта к серваку"
    )
    page = browser.new_page()
    page.context.set_default_timeout(15)
    print("Начало в:", datetime.datetime.now())
    yield page
    browser.close()


@pytest.fixture(scope="function")
def create_local():
    browser = sync_playwright().start().chromium.launch(headless=False)
    page = browser.new_page()
    page.context.set_default_timeout(25000)
    yield page
    browser.close()
