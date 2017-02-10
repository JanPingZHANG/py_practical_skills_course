#!/usr/bin/env python
# encoding: utf-8

from threading import Thread
from multiprocessing import Process
from random import randint
import time

def insertion(ls):
    for i in range(len(ls)):
        j = i
        while j>0 and ls[j] < ls[j-1]:
            temp = ls[j]
            ls[j] = ls[j-1]
            ls[j-1] = temp
            j = j-1

def insertion1000(ls):
    for _ in range(1000):
        insertion(ls)

l1 = [randint(0,100) for _ in range(10000) ]
l2 = [randint(0,100) for _ in range(10000) ]
print('source1: ',l1[:10])
print('source2: ',l2[:10])
r1 = [x for x in l1]
r2 = [x for x in l2]
r3 = [x for x in l1]
r4 = [x for x in l2]

t1 = Thread(target=insertion1000,args=(r1,))
t2 = Thread(target=insertion1000,args=(r2,))
thtime1=time.time()
t1.start()
t2.start()
t1.join()
t2.join()
print(r1[:10])
print(r2[:10])
print('thread spend: ',time.time()-thtime1)

p1 = Process(target=insertion1000,args=(r3,))
p2 = Process(target=insertion1000,args=(r4,))
ptime1=time.time()
p1.start()
p2.start()
p1.join()
p2.join()
print(r3[:10])
print(r4[:10])
print('process spend: ',time.time()-ptime1)

