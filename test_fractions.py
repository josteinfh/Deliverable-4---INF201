import pytest
from fraction_class import Fraction


# 1. Initialization & reduction tests
def test_initialization_and_reduction():
    f1 = Fraction(2, 4)
    assert f1.numerator == 1
    assert f1.denominator == 2

    f2 = Fraction(-6, 9)
    assert f2.numerator == -2
    assert f2.denominator == 3

    f3 = Fraction(5)
    assert f3.numerator == 5
    assert f3.denominator == 1

    f4 = Fraction(0, 7)
    assert f4.numerator == 0
    assert f4.denominator == 1


# 2. Validation tests
@pytest.mark.parametrize("bad_num", [1.5, "2", None, True])
def test_non_integer_numerator(bad_num):
    with pytest.raises(TypeError):
        Fraction(bad_num, 2)


@pytest.mark.parametrize("bad_den", [2.5, "3", None, False])
def test_non_integer_denominator(bad_den):
    with pytest.raises(TypeError):
        Fraction(1, bad_den)


@pytest.mark.parametrize("invalid_den", [0, -1, -10])
def test_non_positive_denominator(invalid_den):
    with pytest.raises(ValueError):
        Fraction(3, invalid_den)


# 3. Comparison tests (==, !=, <, <=, >, >=)
def test_comparisons():
    half = Fraction(1, 2)
    two_fourths = Fraction(2, 4)
    third = Fraction(1, 3)
    neg_half = Fraction(-1, 2)

    # Equal and not equal
    assert half == two_fourths
    assert not (half == third)
    assert half != third
    assert not (half != two_fourths)
    assert Fraction(4, 2) == 2

    # Less than and less than or equal
    assert neg_half < third < half
    assert third <= half
    assert half <= two_fourths
    assert not (half < two_fourths)

    # Greater than and greater than or equal
    assert half > third > neg_half
    assert half >= third
    assert half >= two_fourths
    assert not (third >= half)


# 4. Other special methods tests
def test_str_and_repr():
    assert str(Fraction(3, 4)) == "3/4"
    assert str(Fraction(6, 3)) == "2"
    assert repr(Fraction(2, 4)) == "Fraction(1, 2)"


def test_arithmetic_special_methods():
    a = Fraction(1, 2)
    b = Fraction(1, 3)

    assert a + b == Fraction(5, 6)
    assert a - b == Fraction(1, 6)
    assert a * b == Fraction(1, 6)
    assert a / b == Fraction(3, 2)
    assert Fraction(1, 2) / Fraction(-1, 4) == Fraction(-2, 1)

    with pytest.raises(ZeroDivisionError):
        _ = a / Fraction(0, 1)


def test_unary_and_float_special_methods():
    f = Fraction(-3, 4)
    assert -f == Fraction(3, 4)
    assert abs(f) == Fraction(3, 4)
    assert float(Fraction(1, 4)) == pytest.approx(0.25)