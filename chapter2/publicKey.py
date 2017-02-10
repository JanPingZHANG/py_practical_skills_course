from random import randint,sample

def getData():
	return {x:randint(1,4) for x in sample('abcdefgh',randint(4,8))}

s1 = getData()
s2 = getData()
s3 = getData()
print 's1:',s1
print 's2:',s2
print 's3:',s3

res = []
for key in s1:
	if key in s2 and key in s3:
		res.append(key)
print res

ml = map(dict.viewkeys,[s1,s2,s3])
print ml
print type(ml)
r = reduce(lambda a,b:a&b ,ml)
print r
