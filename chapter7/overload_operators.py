from functools import total_ordering
from abc import abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass
    def __lt__(self,obj):
        return self.area() < obj.area()
    def __eq__(self,obj):
        return self.area() == obj.area()

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width*self.height

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return self.radius**2*3.14

rect = Rectangle(1,2)
c = Circle(1)
print c >= rect
print rect < c
print rect >= c
