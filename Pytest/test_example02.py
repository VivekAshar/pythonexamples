import example02

def test_calc_additon():
    output = example02.calc_additon(2, 4)
    assert output == 6

def test_calc_subtraction():
    output = example02.calc_subtraction(2, 4)
    assert output == -2

def test_calc_multiply():
    output = example02.calc_multiply(2, 4)
    assert output == 8