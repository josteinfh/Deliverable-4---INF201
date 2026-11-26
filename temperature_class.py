

class Temperature:

    # Tolerance for floating-point comparisons
    TOLERANCE = 1e-9



    def __init__(self, value, unit ="C"):
        """Initialize a Temperature instance with a value and unit."""
        unit = unit.upper()

        # Specify the valid units for this class
        valid_units = ['C', 'F', 'K']

        # Check if the unit is valid, if not raise a ValueError
        if unit not in valid_units:
            raise ValueError("Invalid temperature unit. Please use 'C', 'F', or 'K'.")

        # Absolute zero check for each unit, if the value is below absolute zero raise a ValueError
        if (
            (unit == 'C' and value < -273.15)
            or (unit == 'F' and value < -459.67)
            or (unit == 'K' and value < 0)
        ): raise ValueError("Temperature cannot be below absolute zero.")
        
        self._value = float(value)
        self._unit = unit



    # Define read-only properties for value and unit
    @property
    def value(self):
        return self._value

    @property
    def unit(self):
        return self._unit
    

    
    # Converts values from F and K to C 
    def to_celsius(self) -> float:
        if self.unit == 'F':
            return (self.value - 32) * (5/9)
        
        elif self.unit == 'K':
            return (self.value - 273.15)
        
        else:
            return self.value

    # Converts values from C and K to F 
    def to_fahrenheit(self) -> float:
        if self.unit == 'C':
            return (self.value * (9/5)) + 32
        
        elif self.unit == 'K':
            return (self.value - 273.15) * (9/5) + 32
        
        else:
            return self.value

    # Converts values from F and C to K 
    def to_kelvin(self) -> float:
        if self.unit == 'F':
            result = (self.value - 32) * (5/9) + 273.15
            # Check if the result is below absolute zero, if so return 0.0
            if self.TOLERANCE <= result < 0:
                return 0.0
            return result
        
        elif self.unit == 'C':
            return self.value + 273.15
        
        else:
            return self.value

  

    # Function identifies what the target unit is and 
    # calls the appropriate method to calculate new temp
    def convert_to(self, target_unit: str) -> Temperature:
        if target_unit.upper() == 'C':
            new_temp = self.to_celsius()
        elif target_unit.upper() == 'F':
            new_temp = self.to_fahrenheit()
        elif target_unit.upper() == 'K':
            new_temp = self.to_kelvin()
        else:
            raise ValueError("Invalid temperature unit. Please use 'C', 'F', or 'K'.")

        return Temperature(new_temp, target_unit.upper())



    # Define string representation methods for the class
    def __repr__(self) -> str:
        return f'Temperature({self.value}, {self.unit!r})'

    def __str__(self) -> str:
        if self.unit == 'K':
            return f'{self.value:.2f} K'
        else:
            return f'{self.value:.2f} °{self.unit}'



    # Define six comparison methods for the class
    # Comparisons ==
    def __eq__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented

        return abs(self.to_kelvin() - other.to_kelvin()) <= self.TOLERANCE

    # Comparisons !=
    def __ne__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented

        return not self.__eq__(other)

    # Comparisons <
    def __lt__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented

        return self.to_kelvin() < other.to_kelvin() and self.__ne__(other)

    # Comparisons <=
    def __le__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented

        return self.__lt__(other) or self.__eq__(other)

    # Comparisons >
    def __gt__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented

        return self.to_kelvin() > other.to_kelvin() and self.__ne__(other)

    # Comparisons >=
    def __ge__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented

        return self.__gt__(other) or self.__eq__(other)
