import pytest

@pytest.fixture
def clear_book_database() -> None:
    print("[FIXTURE]Очистили БД")

@pytest.fixture
def fill_book_database() -> None:
    print("[FIXTURE] Наполнили БД")


@pytest.mark.usefixtures('fill_book_database')
def test_read_all_books_in_library():
    print("reading all books")

@pytest.fixture()
def initialize_browser_state() -> None:
    chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_butt = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
    email_butt.fill('kira@mail.ru')

    user_butt = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
    user_butt.fill('kira')

    pass_butt = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
    pass_butt.fill('kira')

    reg_butt = chromium_page.get_by_test_id('registration-page-registration-button')
    reg_butt.click()