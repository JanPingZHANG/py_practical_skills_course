
class Shape(object):
    pass

def get_area(shape):
    methods = ('get_area','area','calculate_area')
    for name in methods:
        f = getattr(shape,name,None)
        if f:
            return f()

from operator import methodcaller
def method_area(shape):
    methods = ('get_area','area','calculate_area')
    for name in methods:
        try:
            r = methodcaller(name)(shape)
            if r:
                return r
        except AttributeError:
            pass

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width*self.height
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return self.radius**2*3.14

class Square(Shape):
    def __init__(self,width):
        self.width = width

    def calculate_area(self):
        return self.width**2

rect = Rectangle(2,4)
c = Circle(3)
squ = Square(2)
ls = [rect,c,squ]
for shape in ls:
    print get_area(shape)
print '-'*20
for shape in ls:
    print method_area(shape)

