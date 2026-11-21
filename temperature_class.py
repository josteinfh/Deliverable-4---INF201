

class Temperature:


    def __init__(self, value, unit):
        'Temperature class with value and unit attributes'
        self.value = value
        self.unit = unit
        
        #Specifiy the valid units for this class
        valid_units = ['C', 'F', 'K']

        #if statement returns value error if conditions are not met 
        if unit.upper() not in valid_units or unit.upper() == 'K' and value < 0:
            return ValueError 

    #Converts values from F and K to C 
    def to_celsius(self):
        if self.unit == 'F':
            to_celsius = (self.value - 32) * (5/4)
            if self.unit == 'K':
                to_celsius = (self.value - 273.15)
            return to_celsius


    #Converts values from C and K to F 
    def to_farenheit(self):
        if self.unit == 'C':
            to_farenheit = (self.value * (9/5)) + 32
            if self.unit == 'K':
                to_farenheit = (self.value - 273.15) * (9/5) + 32
            return to_farenheit


    #Converts values from F and C to K 
    def to_kelvin(self):
        if self.unit == 'F':
            to_kelvin = (self.value - 32) * (5/9) + 273.15
            if self.unit == 'C':
                to_kelvin = (self.value + 273.15)
            return to_kelvin

    # Function identifies what the target unit is and 
    # calls the appropriate mothod to calculate new temp
    def convert_to(self, target_unit: str) -> Temperature:
        if target_unit.upper() == 'C':
            new_temp = self.to_celsius()
        elif target_unit.upper() == 'F':
            new_temp = self.to_farenheit()
        elif target_unit.upper() == 'K':
            new_temp = self.to_kelvin()
        else:
            return ValueError
        return new_temp
    
