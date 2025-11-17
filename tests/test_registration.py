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