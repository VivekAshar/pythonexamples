import pytest

    def add(x, y):
        return x + y

    def test_method1():
        assert add(4, 5) == 9
        assert add(4, 4) == 9
