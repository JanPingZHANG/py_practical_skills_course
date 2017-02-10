from itertools import islice

f = open('essay')
for i in islice(f,20):
	print i

print '-'*30
f.seek(0)
for i in islice(f,5):
	print i
