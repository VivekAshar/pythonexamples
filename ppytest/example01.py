import pytest

def add(x, y):
    return x + y


def test_method():  # def test_add():
    assert add(4, 5) == 9
    assert add(5, 4) == 9


