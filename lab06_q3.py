class Converter:
    def __init__(self, length, unit):
        self.length = length
        self.unit = unit.lower()  # Normalize unit to lowercase

    def _to_meters(self):
        if self.unit == "inches":
            return self.length * 0.0254
        elif self.unit == "feet":
            return self.length * 0.3048
        elif self.unit == "yards":
            return self.length * 0.9144
        elif self.unit == "miles":
            return self.length * 1609.34
        elif self.unit == "kilometers":
            return self.length * 1000
        elif self.unit == "meters":
            return self.length
        elif self.unit == "centimeters":
            return self.length * 0.01
        elif self.unit == "millimeters":
            return self.length * 0.001
        else:
            raise ValueError(f"Invalid unit: {self.unit}")

    def inches(self):
        return self._to_meters() / 0.0254

    def feet(self):
        return self._to_meters() / 0.3048

    def yards(self):
        return self._to_meters() / 0.9144

    def miles(self):
        return self._to_meters() / 1609.34

    def kilometers(self):
        return self._to_meters() / 1000

    def meters(self):
        return self._to_meters()

    def centimeters(self):
        return self._to_meters() / 0.01

    def millimeters(self):
        return self._to_meters() / 0.001

c = Converter(9, "inches")
print(c.feet())  
print(c.meters()) 
print(c.centimeters()) 
print(c.kilometers()) 
c2 = Converter(1,"miles")
print(c2.kilometers()) 

    