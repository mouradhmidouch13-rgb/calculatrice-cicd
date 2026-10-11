def addition(a, b):
    return a + b


def soustraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b

def puissance(a, b):
    return a ** b
from calculatrice import addition, soustraction, multiplication, division, puissance

def test_puissance():
    assert puissance(2, 3) == 8

