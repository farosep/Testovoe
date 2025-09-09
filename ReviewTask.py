from time import sleep
import random
from playwright.sync_api import Page, sync_playwright

# Задача1 - Выявить проблемы этих тестов
def test_1():
    wait = 10
    browser = sync_playwright().start().chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://umschool.net/")
    sleep(wait)
    parent_button = page.locator("[data-testid=\'TAB_parent\']")
    parent_button.click()
    sleep(wait)
    subjects = ["Базовая математика", "Английский язык", "История", "Физика"]
    random_subject = random.choice(subjects)
    page.locator(f"//button//span[contains(text(), '{random_subject}')]").click()
    return page


def test_2():
    page = test_1()
    sleep(6)
    page.locator("//*[@id='__nuxt']/main/div/div[6]/div[2]/div[9]/div[1]/div/div[5]/div[2]/a").click()
    page.locator("//button[@data-testid='ADD_PRODUCT_TO_CARD_BUTTON']")
    sleep(8)
    page.locator("//button[@data-testid='ADD_PRODUCT_TO_CARD_BUTTON']").click()
    page.locator("//*[@data-testid='HEADER_CART_BUTTON']").click()
