#Usage of fixtures - resourse setup & clean

import pytest

@pytest.fixture  # decorator
def input_total():
    total = 100
    return total
