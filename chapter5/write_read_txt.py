#-*-coding:utf-8-*-
s = u'你好'
print s
f = open('read_write.txt','w')
b = s.encode('utf8')
print b
f.write(b)
f.close()
 
f = open('read_write.txt','r')
b = f.read()
print b
s = b.decode('utf8')
print s
f.close()
#py2
