from finance_formulas import *

def test_interest():
    val = interest(.01, 1)
    assert round(val, 2) == 1.01


def test_compound():
    val = compound(.08, 4, 5)
    val = round(val, 2)
    assert val == 1.49
    val = compound(1, 4, 1)
    val = round(val, 2)
    assert val == 2.44
    val = 100 * compound(.05, 1, 2)
    val = round(val, 2)
    assert val == 110.25

def test_continous_compound():
    val = continous_compound(.05, 1)
    val = round(val, 4)
    assert val == 1.0513
    val = continous_compound(.05, 2)
    val = round(val, 4)
    assert val == 1.1052
    val = continous_compound(.08, 5)
    val = round(val, 4)
    assert val == 1.4918

