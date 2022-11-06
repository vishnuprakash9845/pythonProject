import pytest


@pytest.mark.run(order=1)
def test_login():
    print("test login")
    assert True


def test_logout():
    print("test logout")
    assert True


def test_customer():
    print("test customer")
    assert True


@pytest.mark.run(order=-2)
def test_product():
    print("test product")
    assert True


@pytest.mark.run(order=5)
def test_user():
    print("test user")
    assert True


@pytest.mark.run(order=4)
def test_admin():
    print("test admin")
    assert True
