

class temperature:
    def __init__(self, value, unit):
        'Temperature class with value and unit attributes'
        self.value = value
        self.unit = unit

        #Specifiy the valid units for this class
        valid_units = ['C', 'F', 'K']

        #if statement returns value error if conditions are not met 
        if unit.upper() not in valid_units or unit.upper() == 'K' and value < 0:
            return ValueError

    def to_celsius(self):
        if self.unit == 'F':
            to_celsius = (self.value * -32) * (5/4)
            if self.unit == 'K':
                to_celsius = (self.value -273.15)
            return to_celsius
