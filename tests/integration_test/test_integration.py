import pytest
from calculator.basic_calc import add, subtract, multiply, divide
from calculator.advanced_calc import square_root, power, logarithm

def perform_operation(a, b, operation):
    try:
        if operation == 'add':
            return add(a, b)
        elif operation == 'subtract':
            return subtract(a, b)
        elif operation == 'multiply':
            return multiply(a, b)
        elif operation == 'divide':
            return divide(a, b)
        elif operation == 'sqrt':
            return square_root(a)
        elif operation == 'power':
            return power(a, b)
        elif operation == 'log':
            return logarithm(a, b)
        else:
            return "Invalid operation"
    except Exception as e:
        return f"Error: {str(e)}"

def test_addition():
    assert perform_operation(2, 3, 'add') == 5

def test_subtraction():
    assert perform_operation(5, 2, 'subtract') == 3

def test_multiplication():
    assert perform_operation(3, 4, 'multiply') == 12

def test_division():
    assert perform_operation(12, 4, 'divide') == 3

def test_square_root():
    assert perform_operation(4, 0, 'sqrt') == 2

def test_power():
    assert perform_operation(2, 3, 'power') == 8

def test_logarithm():
    assert perform_operation(8, 2, 'log') == 3
