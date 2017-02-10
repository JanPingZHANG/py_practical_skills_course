from collections import namedtuple

Student = namedtuple('Student',['name','age','sex','email'])
s = Student('david','24','male','32478@372.com')
print s
print s.name
print s.email
print 'is tuple? : ',isinstance(s,tuple)
