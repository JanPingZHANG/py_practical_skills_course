from random import randint
from collections import deque

q = deque([],3)
n = randint(0,10)
def guess(k):
	if n==k:
		return True
	if k<n:
		print 'the number is smaller'
	else:
		print 'the number is bigger'
	return False

while True:
	print 'you have input ',len(q),' numbers: ',list(q)
	line = raw_input('input a number: ')
	if line.isdigit():
		if guess(int(line)):
			break
		q.append(line)

import pickle
pickle.dump(q,open('history','w'))
r = pickle.load(open('history','r'))
print r
