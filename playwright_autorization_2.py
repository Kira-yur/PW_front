from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    chromium = playwright.chromium.launch(headless=False)
    page = chromium.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = page.locator('//div[@data-testid="login-form-email-input"]//div//input')
    email_input.fill('user.name@gmail.com')

    pass_input = page.locator('//div[@data-testid="login-form-password-input"]//div//input')
    pass_input.fill('Password')

    login_button = page.locator('//button[@data-testid="login-page-login-button"]')
    login_button.click()

    wrong_alert = page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]//div[starts-with(@class, "MuiAlert-message")]')
    expect(wrong_alert).to_be_visible()
    expect(wrong_alert).to_have_text('Wrong email or password123')

    page.wait_for_timeout(5000)


from playwright.sync_api import sync_playwright, expect
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

