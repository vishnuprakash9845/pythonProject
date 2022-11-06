import pytest


@pytest.mark.smoke
@pytest.mark.user
def test_create_user():
    print("test_create_user")


@pytest.mark.regression
@pytest.mark.user
def test_edit_user():
    print("test_edit_user")


@pytest.mark.regression
@pytest.mark.user
def test_delete_user():
    print("test_delete_user")


@pytest.mark.smoke
@pytest.mark.customer
def test_create_customer():
    print("test_create_customer")


@pytest.mark.regression
@pytest.mark.customer
def test_edit_customer():
    print("test_edit_customer")


@pytest.mark.regression
@pytest.mark.customer
def test_delete_customer():
    print("test_delete_customer")


@pytest.mark.smoke
@pytest.mark.product
def test_create_product():
    print("test_create_product")


@pytest.mark.regression
@pytest.mark.product
def test_edit_product():
    print("test_edit_product")


@pytest.mark.regression
@pytest.mark.product
def test_delete_product():
    print("test_delete_product")
