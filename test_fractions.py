import pytest
from fraction_class import Fraction


def test_init_and_reduction():
    assert Fraction(2, 4).numerator == 1
    assert Fraction(2, 4).denominator == 2
    assert Fraction(-6, 9).numerator == -2
    assert Fraction(-6, 9).denominator == 3
    assert Fraction(5).numerator == 5
    assert Fraction(5).denominator == 1
    assert Fraction(0, 7).numerator == 0
    assert Fraction(0, 7).denominator == 1


@pytest.mark.parametrize("bad_value", [1.5, "2", None, True, False])
def test_non_integer_arguments(bad_value):
    with pytest.raises(TypeError):
        Fraction(bad_value, 2)
    with pytest.raises(TypeError):
        Fraction(2, bad_value)


@pytest.mark.parametrize("bad_den", [0, -1, -5])
def test_non_positive_denominator(bad_den):
    with pytest.raises(ValueError):
        Fraction(1, bad_den)


def test_comparisons():
    a = Fraction(1, 2)
    b = Fraction(2, 4)
    c = Fraction(1, 3)
    neg = Fraction(-1, 2)

    assert a == b
    assert a != c
    assert Fraction(4, 2) == 2
    assert neg < c < a
    assert c <= a
    assert a <= b
    assert a > c > neg
    assert a >= c
    assert a >= b


def test_string_representations():
    assert str(Fraction(3, 4)) == "3/4"
    assert str(Fraction(6, 3)) == "2"
    assert repr(Fraction(2, 4)) == "Fraction(1, 2)"


def test_arithmetic_and_unary():
    x = Fraction(1, 2)
    y = Fraction(1, 3)

    assert x + y == Fraction(5, 6)
    assert x - y == Fraction(1, 6)
    assert x * y == Fraction(1, 6)
    assert x / y == Fraction(3, 2)
    assert -x == Fraction(-1, 2)
    assert abs(Fraction(-3, 4)) == Fraction(3, 4)
    assert float(Fraction(1, 4)) == pytest.approx(0.25)

    with pytest.raises(ZeroDivisionError):
        _ = x / Fraction(0, 1)