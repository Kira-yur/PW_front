from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
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

    context.storage_state(path='browser-stage.json')



with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-stage.json')
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')

    page.wait_for_timeout(5000) 