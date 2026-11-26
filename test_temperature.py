import pytest
from temperature_class import Temperature

TOLERANCE = Temperature.TOLERANCE


# 1. Initialization tests
def test_default_unit():
    t = Temperature(25)
    assert t.unit == "C"
    assert t.value == 25


def test_case_insensitive():
    assert Temperature(25, "c").unit == "C"
    assert Temperature(25, "f").unit == "F"
    assert Temperature(25, "k").unit == "K"


def test_read_only():
    t = Temperature(25, "C")

    with pytest.raises(AttributeError):
        t.value = 30

    with pytest.raises(AttributeError):
        t.unit = "F"


# 2. Validation tests
def test_invalid_unit():
    with pytest.raises(ValueError):
        Temperature(25, "X")


def test_below_absolute_zero():
    with pytest.raises(ValueError):
        Temperature(-274, "C")

    with pytest.raises(ValueError):
        Temperature(-460, "F")

    with pytest.raises(ValueError):
        Temperature(-1, "K")


# 3. Conversion tests
@pytest.mark.parametrize(
    "C, F, K",
    [
        (-273.15, -459.67, 0),    # Absolute zero
        (-40, -40, 233.15),       # Celsius-Fahrenheit crossover
        (0, 32, 273.15),          # Freezing point of water
        (37, 98.6, 310.15),       # Human body temperature
        (100, 212, 373.15),       # Boiling point of water
    ],
)
def test_conversion(C, F, K):
    t_c = Temperature(C, "C")
    assert abs(t_c.to_fahrenheit() - F) <= TOLERANCE
    assert abs(t_c.to_kelvin() - K) <= TOLERANCE

    t_f = Temperature(F, "F")
    assert abs(t_f.to_celsius() - C) <= TOLERANCE
    assert abs(t_f.to_kelvin() - K) <= TOLERANCE

    t_k = Temperature(K, "K")
    assert abs(t_k.to_celsius() - C) <= TOLERANCE
    assert abs(t_k.to_fahrenheit() - F) <= TOLERANCE


# 4. Round-trip conversion tests ("C" -> "F" -> "K" -> "C")
@pytest.mark.parametrize("C", [-273.15, -40, 0, 37, 100])
def test_round_trip_conversion(C):
    t_c = Temperature(C, "C")
    t_f = Temperature(t_c.to_fahrenheit(), "F")
    t_k = Temperature(t_f.to_kelvin(), "K")
    round_tripped_c = t_k.to_celsius()

    assert abs(round_tripped_c - C) <= TOLERANCE


# 5. Cross-unit comparisons
def test_comparisons_across_units():
    freezing_c = Temperature(0, "C")
    freezing_f = Temperature(32, "F")
    boiling_k = Temperature(373.15, "K")
    warm_f = Temperature(68, "F")      # 20°C

    # Equality
    assert freezing_c == freezing_f
    assert not (freezing_c == boiling_k)

    # Strict inequalities
    assert freezing_c < boiling_k
    assert freezing_f < warm_f
    assert boiling_k > freezing_c
    assert warm_f > freezing_f

    # Non-strict inequalities
    assert freezing_c <= freezing_f
    assert freezing_c <= boiling_k
    assert boiling_k >= freezing_c
    assert freezing_f >= freezing_c


# 6. Formatting tests
def test_str_and_repr():
    t = Temperature(25, "C")

    assert str(t) == "25°C"
    assert repr(t) == "Temperature(25, 'C')"