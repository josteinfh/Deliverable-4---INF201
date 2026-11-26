import math


class Fraction:
    """Represents a rational number with integer numerator and strictly positive denominator."""

    def __init__(self, numerator: int, denominator: int = 1):
        if isinstance(numerator, bool) or not isinstance(numerator, int):
            raise TypeError("Numerator must be an integer.")
        if isinstance(denominator, bool) or not isinstance(denominator, int):
            raise TypeError("Denominator must be an integer.")
        if denominator <= 0:
            raise ValueError("Denominator must be strictly positive (> 0).")

        common = math.gcd(numerator, denominator)
        self._numerator = numerator // common
        self._denominator = denominator // common

    @property
    def numerator(self) -> int:
        return self._numerator

    @property
    def denominator(self) -> int:
        return self._denominator

    #String representations 
    def __str__(self) -> str:
        if self._denominator == 1:
            return str(self._numerator)
        return f"{self._numerator}/{self._denominator}"

    def __repr__(self) -> str:
        return f"Fraction({self._numerator}, {self._denominator})"

    # Auxiliary function to determine if input 'other' is a fraction, and coerce it into being
    # a fraction if it is an integer. 
    @staticmethod
    def _coerce(other):
        if isinstance(other, Fraction):
            return other
        if isinstance(other, int) and not isinstance(other, bool):
            return Fraction(other, 1)
        return NotImplemented

    # All 6 comparison methods
    def __eq__(self, other) -> bool:
        other_frac = self._coerce(other)
        if other_frac is NotImplemented:
            return False
        return (
            self._numerator == other_frac._numerator
            and self._denominator == other_frac._denominator
        )

    def __ne__(self, other) -> bool:
        return not (self == other)

    def __lt__(self, other) -> bool:
        other_frac = self._coerce(other)
        if other_frac is NotImplemented:
            return NotImplemented
        return self._numerator * other_frac._denominator < other_frac._numerator * self._denominator

    def __le__(self, other) -> bool:
        other_frac = self._coerce(other)
        if other_frac is NotImplemented:
            return NotImplemented
        return self._numerator * other_frac._denominator <= other_frac._numerator * self._denominator

    def __gt__(self, other) -> bool:
        other_frac = self._coerce(other)
        if other_frac is NotImplemented:
            return NotImplemented
        return self._numerator * other_frac._denominator > other_frac._numerator * self._denominator

    def __ge__(self, other) -> bool:
        other_frac = self._coerce(other)
        if other_frac is NotImplemented:
            return NotImplemented
        return self._numerator * other_frac._denominator >= other_frac._numerator * self._denominator

    # Additional 'special' methods for fraction addition, subtraction, multiplication and division
    def __add__(self, other) -> "Fraction":
        other_frac = self._coerce(other)
        if other_frac is NotImplemented:
            return NotImplemented
        num = self._numerator * other_frac._denominator + other_frac._numerator * self._denominator
        den = self._denominator * other_frac._denominator
        return Fraction(num, den)

    def __sub__(self, other) -> "Fraction":
        other_frac = self._coerce(other)
        if other_frac is NotImplemented:
            return NotImplemented
        num = self._numerator * other_frac._denominator - other_frac._numerator * self._denominator
        den = self._denominator * other_frac._denominator
        return Fraction(num, den)

    def __mul__(self, other) -> "Fraction":
        other_frac = self._coerce(other)
        if other_frac is NotImplemented:
            return NotImplemented
        return Fraction(
            self._numerator * other_frac._numerator,
            self._denominator * other_frac._denominator,
        )

    def __truediv__(self, other) -> "Fraction":
        other_frac = self._coerce(other)
        if other_frac is NotImplemented:
            return NotImplemented
        if other_frac._numerator == 0:
            raise ZeroDivisionError("Cannot divide by a zero fraction.")
        num = self._numerator * other_frac._denominator
        den = self._denominator * other_frac._numerator
        if den < 0:
            num, den = -num, -den
        return Fraction(num, den)
    
    def __neg__(self) -> "Fraction":
        return Fraction(-self._numerator, self._denominator)

    def __abs__(self) -> "Fraction":
        return Fraction(abs(self._numerator), self._denominator)

    def __float__(self) -> float:
        return self._numerator / self._denominator

