import pytest

@pytest.mark.parametrize("city",["Agra","Bangalore","Chennai","Delhi"])
def test_demo1(city):
    print("test demo1",city)
