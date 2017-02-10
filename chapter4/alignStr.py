import string
from random import sample,randint

s = string.ascii_lowercase
d = dict()
for i in range(10):
	d[''.join(sample(s,randint(3,10)))] = randint(100,10000)
print d
length = max(map(lambda x:len(x),d.keys()))
r = ''
for k in d:
	r = r + str(k).ljust(length)+':'+str(d[k])+'\n'
print r
