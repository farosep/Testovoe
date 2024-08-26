import pytest
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def create_remote():
    remote_options = Options()
    remote_options.add_argument("--use-fake-ui-for-media-stream")
    remote_options.add_argument("--use-fake-device-for-media-stream")
    remote_options.add_argument("--disable-dev-shm-usage")

    # remote_options.page_load_strategy = 'eager'
    remote_options.set_capability(
        'selenoid:options',
        {
            "browserName": "chrome",
            "browserVersion": "121.0",
            "sessionTimeout": "3m",  # можно управлять таймаутом отключения
            'enableVNC': True,
            'enableVideo': True
        }
    )
    driver = webdriver.Remote(
        options=remote_options
    )
    timeout = 15
    driver.set_page_load_timeout(timeout)
    driver.maximize_window()
    print("Начало в:", datetime.datetime.now())
    yield driver


@pytest.fixture(scope="function")
def create_browser():
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--remote-debugging-port=8888")
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_page_load_timeout(15)
    driver.maximize_window()
    yield driver
    driver.quit()
