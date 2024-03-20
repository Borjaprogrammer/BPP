# test_pytest.py
import pytest

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("¡No se puede dividir por cero!")
    return a / b

def test_suma():
    assert suma(3, 5) == 8
    assert suma(-3, 5) == 2
    assert suma(0, 0) == 0

def test_resta():
    assert resta(5, 3) == 2
    assert resta(-3, 5) == -8
    assert resta(0, 0) == 0

def test_multiplicacion():
    assert multiplicacion(3, 5) == 15
    assert multiplicacion(-3, 5) == -15
    assert multiplicacion(0, 5) == 0

def test_division():
    assert division(10, 2) == 5
    assert division(-10, 2) == -5
    assert division(0, 5) == 0

def test_division_por_cero():
    with pytest.raises(ValueError):
        division(10, 0)

print("ok")