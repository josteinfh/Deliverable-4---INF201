
import pytest
from temperature_class import Temperature
TOLERANCE = Temperature.TOLERANCE

# 1. Initialization tests
# Test: Default unit
def test_default_unit():
    t = Temperature(25)
    assert t.unit == "C"
    assert t.value == 25

# Test: Case insensitive unit
def test_case_insensitive():
    assert Temperature(25, "c").unit == "C"
    assert Temperature(25, "f").unit == "F"
    assert Temperature(25, "k").unit == "K"

# Test: Read-only behavior
def test_read_only():
    t = Temperature(25, "C")

    with pytest.raises(AttributeError):
        t.value = 30

    with pytest.raises(AttributeError):
        t.unit = "F"



# 2. Validation tests
# Test: Invalid unit
def test_invalid_unit():
    with pytest.raises(ValueError):
        Temperature(25, "X")

# Test: Below absolute zero
def test_below_absolute_zero():
    with pytest.raises(ValueError):
        Temperature(-274, "C")

    with pytest.raises(ValueError):
        Temperature(-460, "F")

    with pytest.raises(ValueError):
        Temperature(-1, "K")



# 3. Conversion tests
@pytest.mark.parametrize("C, F, K", [
    (-273.15, -459.67, 0),  # Absolute zero
    (-40, -40, 233.15),     # Celsius-Fahrenheit crossover
    (0, 32, 273.15),        # Freezing point of water
    (37, 98.6, 310.15),     # Human body temperature
    (100, 212, 373.15),     # Boiling point of water
])
def test_conversion(C, F, K):
    t = Temperature(C, "C")
    assert abs(t.to_fahrenheit() - F) <= TOLERANCE
    assert abs(t.to_kelvin() - K) <= TOLERANCE

    t = Temperature(F, "F")
    assert abs(t.to_celsius() - C) <= TOLERANCE
    assert abs(t.to_kelvin() - K) <= TOLERANCE

    t = Temperature(K, "K")
    assert abs(t.to_celsius() - C) <= TOLERANCE
    assert abs(t.to_fahrenheit() - F) <= TOLERANCE



# 4. Round-trip conversion tests
@pytest.mark.parametrize("C", [-273.15, -40, 0, 37, 100])
def test_round_trip_conversion(C):
    t_f = Temperature(C, "C")
    t_k = t_f.to_fahrenheit()
    t_c = t_f.to_kelvin()

    # Convert back to Celsius