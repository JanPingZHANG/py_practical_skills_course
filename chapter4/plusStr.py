
s = list('abcdefghiklmnopq')
print s
r = reduce(lambda x,y:x+y,s)
print 'result: ',r

print 'str.jion method: ',''.join(s)
