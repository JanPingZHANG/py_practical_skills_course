from random import randint
from collections import OrderedDict
from time import time

start = time()
d = OrderedDict()
players = list('ABCDEFLH')
for i in range(8):
	raw_input()
	p = players.pop(randint(0,7-i))
	t = time() - start
	print i,p,t,
	d[p] = (i,t)
print
print '-'*20
for k in d:
	print k,d[k]

