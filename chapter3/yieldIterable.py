
def f():
	print '1 in f()'
	yield 1
	print '2 in f()'
	yield 2
	print '3 in f()'
	yield 3

'''
g = f()
print g.next() 
print g.next() 
print g.next() 
print g.next() 
for i in g:
	print i
'''

class PrimeNumIterable:
	def __init__(self,start,end):
		self.start = start
		self.end = end
	def isPrimeNum(self,x):
		if x<2:
			return False
		for i in range(2,x):
			if x % i ==0:
				return False
		return True
	def __iter__(self):
		for i in range(self.start,self.end+1):
			if self.isPrimeNum(i):
				yield i
	

p = PrimeNumIterable(0,100)
for i in p:
print i
