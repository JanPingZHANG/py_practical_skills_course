class Circle(object):
    def __init__(self,radius):
        self._radius = radius
    def setradius(self,value):
        if not isinstance(value,(int,long,float)) and value>0:
            raise TypeError('the value is not digital')
        self._radius = value
    def getradius(self):
        return self._radius
    Radius = property(getradius,setradius)
    #Radius = property(getradius,None)

c = Circle(3)
print c.Radius
c._radius = 5
print c.Radius
c.Radius = 'ab'

