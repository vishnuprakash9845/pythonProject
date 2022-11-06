import pytest


@pytest.mark.dependency(name="createuser")
def test_createuser():
    print("test_createuser")
    assert True


@pytest.mark.dependency(depends=["createuser"])
def test_deleteuser():
    print("test_deleteuser")
    assert True
