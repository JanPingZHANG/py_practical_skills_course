
class FloatRange:
	def __init__(self,start,end,step=0.1):
		self.start = start
		self.end = end
		self.step = step
	def __iter__(self):
		t = self.start
		while t<=self.end:
			yield t
			t = t + self.step
	def __reversed__(self):
		t = self.end
		while t>=self.start:
			yield t
			t = t - self.step

f = FloatRange(1,5,0.5)
for i in f:
	print i
print
print '-'*30
print
for i in reversed(f):
	print i
print 
print '+'*30
print
for i in f.__reversed__():
	print i
