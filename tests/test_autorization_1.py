from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.autorization
def test_autorization(chromium_page: Page):

    with sync_playwright() as playwright:
        chromium = playwright.chromium.launch(headless=False)
        page = chromium.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        email_input = page.get_by_test_id('login-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')

        pass_input = page.get_by_test_id('login-form-password-input').locator('input')
        pass_input.fill('Password')

        login_button = page.get_by_test_id('login-page-login-button')
        login_button.click()

        wrong_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')
        expect(wrong_alert).to_be_visible()
        expect(wrong_alert).to_have_text('Wrong email or password')

