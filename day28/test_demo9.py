import pytest


@pytest.fixture(autouse=True)
def login_logout():
    print("login")
    yield
    print("logout")

def test_create_user():
    print("test_create_user")

def test_edit_user():
    print("test_edit_user")


def test_delete_user():
    print("test_delete_user")
