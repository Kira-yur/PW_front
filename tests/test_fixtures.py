import pytest


@pytest.fixture (autouse=True)
def send_analytics_data():
    ...