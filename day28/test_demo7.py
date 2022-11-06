import pytest


@pytest.fixture()
def login():
    print("1 login 1")


@pytest.mark.usefixtures("login")
def test_create_user():
    print("test_create_user")


@pytest.mark.usefixtures("login")
def test_edit_user():
    print("test_edit_user")


@pytest.mark.usefixtures("login")
def test_delete_user():
    print("test_delete_user")
