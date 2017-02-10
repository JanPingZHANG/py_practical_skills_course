from random import sample,randint
#l1 = [x for x in sample('abdceghik',randint(5,9))]
#print l1
#s1 = set(l1)
s1,s2,s3 = map(set,[[x for x in sample('abdceghiknmopqrst',randint(5,9))] for i in range(3)])

print s1,s2,s3
t = frozenset(s1)
print t
# error: print s1[0]
# error: t.add('z')

print 's1&s2',s1&s2
print 's1^s2',s1^s2
s1.add(1)
print 's1.add(1): ',s1
s1.update('ABCDEF')
print 's1.update("ABCDEF"): ',s1
s1.remove('A')
print 's1.remove("A"): ',s1
print 's1.union(s2) ',s1.union(s2)
print 's1 and s2 is s1 ',(s1 and s2)
print 's1 or s2 is s2 ',(s1 or s2)
print 's1 - s2 is s1.difference(s2)',s1.difference(s2)

