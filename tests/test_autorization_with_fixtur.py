import pytest
from playwright.sync_api import sync_playwright, Page



@pytest.mark.autorization
def test_autorization(chromium_page: Page):
        chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')

        pass_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
        pass_input.fill('Password')

        login_button = chromium_page.get_by_test_id('login-page-login-button')
        login_button.click()

        wrong_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
        expect(wrong_alert).to_be_visible()
        expect(wrong_alert).to_have_text('Wrong email or password')

