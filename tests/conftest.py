from playwright.sync_api import sync_playwright, Page
import pytest

@pytest.fixture
def chromium_page() -> Page: #Данная фикстура возвращает объект Page
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()