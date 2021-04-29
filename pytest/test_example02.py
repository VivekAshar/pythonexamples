import example02

def test_calc_additon():  # def test_method()
    output = example02.calc_additon(2, 4)
    assert output == 6

def test_calc_subtraction(): # def test_method()
    output = example02.calc_subtraction(2, 4)
    assert output == -2

def test_calc_multiply():
    output = example02.calc_multiply(2, 4)
    assert output == 8

def test_calc_addition():
    output = example02.calc_additon(1,1)
    assert output == 2

def test_calc_addition():
    output = example02.calc_additon(1,1)
    assert output == 5