from math import pi

class CircleMeasurements():
    def __init__(self, radius):
        self.radius = radius


    def radius_of_circle(self, radius: float) -> float:
        return self.radius


    def diameter_of_circle(self, radius: float) -> float:
        return self.radius * 2
       
    def circumference_of_circle(self, radius: float) -> float:
        return pi * self.radius * 2


    def area_of_circle(self, radius: float) -> float:
        return pi * self.radius ** 2


new_circle = CircleMeasurements(10)

print('Radius: ', new_circle.radius_of_circle(10))
