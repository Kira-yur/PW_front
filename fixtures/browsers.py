import pytest
from playwright.sync_api import Page, Playwright


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
        browser = playwright.chromium.launch(headless=False)
        yield browser.new_page()
        browser.close()



@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_butt = page.get_by_test_id('registration-form-email-input').locator('input')
    email_butt.fill('kira@mail.ru')

    user_butt = page.get_by_test_id('registration-form-username-input').locator('input')
    user_butt.fill('kira')

    pass_butt = page.get_by_test_id('registration-form-password-input').locator('input')
    pass_butt.fill('kira')

    reg_butt = page.get_by_test_id('registration-page-registration-button')
    reg_butt.click()

    context.storage_state(path="browser-stage.json")
    browser.close()

@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-stage.json")
    yield context.new_page()
    browser.close()