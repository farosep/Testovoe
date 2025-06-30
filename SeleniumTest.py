from time import sleep
import random
from playwright.sync_api import Page, sync_playwright

# Задача1 - Выявить проблемы этих тестов
def test_1():
    wait = random.randint(5, 20)
    browser = sync_playwright().start().chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://umschool.net/")
    sleep(wait)
    parent_button = page.locator("[data-testid=\'TAB_parent\']")
    parent_button.click()
    sleep(wait)
    page.locator("a:nth-child(1) > div:nth-child(2) > span").click()
    return page


def test_2():
    page = test_1()
    sleep(25)
    page.locator("div:nth-child(3) > div > div.relative.flex.flex-col.h-full > .mt-auto > a")
    page.locator("main > div > div.ui-radius-md.ums-card.ums-component-root.ui-bg-grey-0.ui-px-3.ui-py-4.sm\:ui-p-4.md\:ui-p-5.lg\:ui-p-8.space-y-8.sm\:space-y-10.lg\:space-y-20.my-8.md\:my-20 > div > div > div > div.base-slider.base-slider--with-offset.base-slider--full-height > div.base-slider__area.no-scrollbar > div:nth-child(3)").click()
    sleep(17)
    child = page.locator("li:nth-child(1) > div > div")
    page.locator("li:nth-child(1) > div > div > div.p-5.w-full.grid.grid-cols-1.gap-x-4.sm\:grid-cols-\[1fr_170px\].md\:grid-cols-\[1fr_220px\].md\:gap-x-8 > div.flex.flex-col.justify-end.sm\:justify-between.mt-7.sm\:mt-0 > div.mt-5.md\:mt-0.flex.relative.w-full > div > button").click()
    page.locator("#__nuxt > div.sticky.z-10 > header > div > div > div.cmp-flex.cmp-items-center.cmp-justify-end.cmp-gap-3.md\:cmp-gap-5 > div.relative").click()
    sleep(15)
    page.locator("#__nuxt > main > div.mx-auto.w-\[1446px\].max-w-full.p-container > div.grid.gap-x-4.grid-cols-1.md\:grid-cols-\[3\.3fr_1fr\].items-start > div:nth-child(1) > div.relative > ul > li > div > div.p-4.sm\:p-0.divide-y-\[1px\].divide-grey-800\/10 > div.mb-4 > h3")
