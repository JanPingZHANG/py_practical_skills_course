from random import randint

data = [randint(-10,10) for _ in xrange(10)]
print 'origin data is: ',data
newData = filter(lambda x:x>=0,data)
print 'filter data... '
print 'data: ',newData

newData = [x for x in data if x>=0]

d = set(data)
print 'set is ',d
dd = {x for x in d if x%3==0}
print '%3==0: ',dd
