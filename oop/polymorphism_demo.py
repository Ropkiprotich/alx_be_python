import math
class Shape:
    def area(self):
        return "NotImplementedError."

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width =width
    def area(self):
        cal_area = self.length * self.width
        return cal_area

        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        cal_area = math.pi * (self.radius) ** 2
        return cal_area

    