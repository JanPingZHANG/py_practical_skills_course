from random import randint

data = {x:randint(60,100) for x in 'abcdefghk'}
print data
t = zip(data.itervalues(),data.iterkeys())
print sorted(t)
r = sorted(data.items(),key=lambda item:item[1])
print r
