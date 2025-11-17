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