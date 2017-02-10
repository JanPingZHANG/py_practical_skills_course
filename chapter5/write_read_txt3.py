#-*-coding:utf-8-*-

s = '你好'
print(s)
f = open('write_read.txt','wt',encoding='utf8')
f.write(s)
f.close()

f = open('write_read.txt','rt',encoding='utf8')
r = f.read()
print(r)
