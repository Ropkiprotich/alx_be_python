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
        return f"The area of the rectangle is:{cal_area}"

        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        cal_area = math.pi * (self.radius)**2
        return f"The area of the circle is: {cal_area}"

    