from calculatrice import (
    addition,
    soustraction,
    multiplication,
    division,
    puissance,
)


def test_addition():
    assert addition(2, 3) == 5


def test_soustraction():
    assert soustraction(5, 2) == 3


def test_multiplication():
    assert multiplication(3, 4) == 12


def test_division():
    assert division(10, 2) == 5


def test_division_par_zero():
    try:
        division(5, 0)
        assert False
    except ValueError:
        assert True


def test_puissance():
    assert puissance(2, 3) == 8
