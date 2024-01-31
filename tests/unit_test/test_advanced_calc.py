import pytest
from calculator.advanced_calc import square_root, power, logarithm

def test_square_root():
    assert square_root(4) == 2
    assert square_root(9) == 3
    assert square_root(0) == 0

    with pytest.raises(ValueError):
        square_root(-1)

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(-2, 3) == -8
    assert power(2, -2) == 0.25

def test_logarithm():
    assert logarithm(100) == 2
    assert logarithm(100, 10) == 2
    assert logarithm(1) == 0
    assert logarithm(10, 2) == pytest.approx(3.3219, 0.0001)

    with pytest.raises(ValueError):
        logarithm(-1)

    with pytest.raises(ValueError):
        logarithm(0)
