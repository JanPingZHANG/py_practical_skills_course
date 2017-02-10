l=list('abcdef')
l.extend([1,2,3])
print l
print ','.join(str(x) for x in l)
