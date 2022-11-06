import pytest


@pytest.mark.parametrize("city",[("Agra","North"),("Chennai","South")])
def test_demo1(city):
    print("--")
    for v in city:
        print("test demo1",v)

    print("--")