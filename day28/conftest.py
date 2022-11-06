import pytest


@pytest.fixture(autouse=True)
def login():
    print("login")

@pytest.fixture(autouse=True)
def logout():
    yield
    print("logout")
