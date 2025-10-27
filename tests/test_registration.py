from playwright.sync_api import sync_playwright, Page, expect
import pytest

@pytest.mark.regression
@pytest.mark.registration
def test_registration_success(chromium_page: Page):
        chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        email_butt = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
        email_butt.fill('kira@mail.ru')

        user_butt = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
        user_butt.fill('kira')

        pass_butt = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
        pass_butt.fill('kira')

        reg_butt = chromium_page.get_by_test_id('registration-page-registration-button')
        reg_butt.click()

        dashbord_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
        expect(dashbord_title).to_be_visible()

        chromium_page.context.storage_state(path='browser-stage.json')

        chromium_page.wait_for_timeout(1000)

        chromium_page.close()

from playwright.sync_api import sync_playwright, Page, expect
import pytest

        chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')

        dashbord_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
        expect(dashbord_title).to_be_visible()

        chromium_page.wait_for_timeout(1000)


    # with sync_playwright() as playwright:
    #     browser = playwright.chromium.launch(headless=False)
    #     context = browser.new_context(storage_state='browser-stage.json')
    #     page = context.new_page()
    #
    #     page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
    #
    #     page.wait_for_timeout(5000)