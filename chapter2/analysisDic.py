from random import randint
d = {x:randint(60,100) for x in xrange(1,21)}
print 'origin data: ',d
d90 = {k:v for k,v in d.iteritems() if v>=90}
print '>90: ',d90
