import re
from random import randint

SOURCE = 'abcdefghijklmnopqrst,;?\t\n'
s = ''
for i in range(50):
	s = s + SOURCE[randint(0,len(SOURCE)-1)]

def splitStr(s,ds):
	res = [s]
	for d in ds:
		t = []
		map(lambda x:t.extend(x.split(d)),res)
		res = t
	return [x for x in res if x]

print 'origin:   ',s
r = splitStr(s,',;?\t\n')
print 'result:   ',r

print re.split(r'[,;?\t\n]+',s)
