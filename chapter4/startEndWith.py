
s = ['a.cpp','b.c','d.java','e.cs','f.py','h.sh']
r = [name for name in s if name.endswith(('.py','.sh'))]
print r

s = ['a1','b3','a4','d5']
r = [name for name in s if name.startswith(('a','b'))]
print r
