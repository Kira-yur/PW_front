import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9)])
def test_several_number(number: int, expected: int):
    assert number ** 2 == expected


@pytest.mark.parametrize('os', ['macos', 'windows', 'linux', 'debian'])
@pytest.mark.parametrize('browser', ['chromium', 'webkit', 'firefox'])
def test_multiplications_of_number(os: str, browser: str):
    assert len(os + browser) > 0


@pytest.fixture(params=['chromium', 'webkit', 'firefox'])
def browser(request: SubRequest):  # вот тут подключаем и делаемм импорт, нихуя не понятно
    return request.param  # вот тут тоже че к чему


def test_open_browser(
        browser: str):  # 1. после названия пробел нельзя делать? 2. анотирование, когда и зачем. 3. зачем надо двоеточие в конце
    print(f'Running test on browser: {browser}')

@pytest.mark.parametrize('user', ['Alise', 'Zara'])
class TestOperations:
    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])
    def test_user_with_operations(self, user: str, account: str):
        print(f'User with operations: {user}')
    def test_user_without_operations(self, user: str):
        print(f'User without operations: {user}')