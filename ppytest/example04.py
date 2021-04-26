#Usage of fixtures - resourse setup & clean

import pytest

@pytest.fixture
def input_total():
    total = 100
    return total
