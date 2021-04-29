import pytest

@pytest.mark.parametrize("num, output",[(1,12),(2,13),(3,14),(4,15),(5,16)])
def test_multiplication_11(num, output):
    assert 11+num == output