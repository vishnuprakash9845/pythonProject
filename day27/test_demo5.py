import pytest

@pytest.mark.run(order=3)
@pytest.mark.dependency(name="login")
def test_login():
    print("test login")
    assert True

@pytest.mark.run(order=2)
@pytest.mark.dependency(name="createuser")
def test_createuser():
    print("test_createuser")
    assert True

@pytest.mark.run(order=1)
@pytest.mark.dependency(depends=["createuser","login"])
def test_deleteuser():
    print("test_deleteuser")
    assert True


