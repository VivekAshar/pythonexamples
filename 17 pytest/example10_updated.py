import pytest
import example10


@pytest.mark.parametrize(“test_input, expected_output”,[(5, 25), (6, 36), (7, 49)])
def test_cal_square(test_input, expected_output):
    result = example10.cal_square(test_input)
    assert result == expected_output
