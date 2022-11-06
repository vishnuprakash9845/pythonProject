import pytest

@pytest.fixture()
def login():
    print("login")

def test_create_user(login):
    print("test_create_user")

def test_edit_user(login):
    print("test_edit_user")

def test_delete_user(login):
    print("test_delete_user")
