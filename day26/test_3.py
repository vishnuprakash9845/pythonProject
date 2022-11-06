import pytest


class TestDemo1:
    def test_demo1(self):
        print("This is my test demo 1")

class TestDemo2:

    @pytest.mark.skip
    def test_demob(self):
        print("This is my test demo b")

    @pytest.mark.skip(reason="known issue A123")
    def test_demoa(self):
        print("This is my test demo a")

    a=10
    b=2

    @pytest.mark.skipif(a>b,reason="a is >b")
    def test_democ(self):
        print("This is my test demo c")