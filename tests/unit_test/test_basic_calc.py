import pytest
from ...calculator.basic_calc import add, subtract, multiply, divide

def test_add():
    assert add(5, 3) == 8
    assert add(-1, 1) == 0
    assert add(-4, -6) == -10

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(2, 3) == -1
    assert subtract(-10, -5) == -5

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
    assert multiply(5, 0) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(-6, 3) == -2

    with pytest.raises(ValueError):
        divide(5, 0)  # Test for division by zero
