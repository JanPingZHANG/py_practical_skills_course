s = '     abc      '
print s
print s.strip()
print s.lstrip()
print s.rstrip()

import re
import string
from random import sample,randint

source = string.ascii_lowercase +'\r\n\t?!:'
source = source*3
s = ''.join(sample(source,randint(50,80)))
print s
r = re.sub('[\r\n\t?!:]','',s)
print r
print r.translate(string.maketrans('abc','xyz'),'ghijk')
