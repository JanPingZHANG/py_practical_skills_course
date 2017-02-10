from random import randint

data = [randint(0,21) for _ in xrange(20)]
print data
d = dict.fromkeys(data,0)
for x in data:
	d[x] = d[x] + 1
sordata = sorted(d.items(),key=lambda item:item[1],reverse=True)
print sordata
from collections import Counter
r = Counter(data)
print r
print r.most_common(3)

import re
txt = open('test.txt').read()
li = re.split('\W+',txt)
c = Counter(li)
print c.most_common(5)
