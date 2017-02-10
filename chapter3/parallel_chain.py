from itertools import chain
import string
from collections import OrderedDict
from random import randint

ALPHA = string.ascii_lowercase
def init_scores():
	r = OrderedDict()
	for i in ALPHA:
		r[i] = randint(60,100)
	return r

english = init_scores()
chinese = init_scores()
math = init_scores()
for i in zip(english.keys(),english.values(),chinese.values(),math.values()):
	print i
print '-'*20
for i in chain(english.keys(),english.values(),chinese.values(),math.values()):
	print i
