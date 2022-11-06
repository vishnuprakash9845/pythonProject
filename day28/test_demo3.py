import pytest

@pytest.mark.parametrize("login",[("admin","manager"),("trainee","trainee")])
def test_login(login):
    print("open the browser")
    print("enter the url")
    print("Enter the un",login[0])
    print("Enter the pw",login[1])
    print("Click on login button")
    print("verify homepage is displayed")