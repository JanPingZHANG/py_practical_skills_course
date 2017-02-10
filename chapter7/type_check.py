
class Attr(object):
    def __init__(self,name,_type):
        self.name = name
        self._type = _type
    def __get__(self,instance,cls):
        print 'in __get__'
        return instance.__dict__[self.name]
    def __set__(self,instance,value):
        if not isinstance(value,self._type):
            raise TypeError('expected type %s'%type(value))
        instance.__dict__[self.name] = value
        print 'in __set__'
    def __delete__(self,instance):
        print 'in __delete__'
        del instance.__dict__[self.name]

class Person(object):
    name = Attr('name',str)
    age = Attr('age',int)
    def __init__(self,name,age):
		self.name = name
		self.age = age

p = Person('david',24)
print p.name
del p.name
#error print p.name
p.age = '24'
