#!/usr/bin/env python
# encoding: utf-8

from multiprocessing import Process,Pipe,Queue
from time import sleep

def f(q):
    print('start child process')
    print(q.get())
    print('end child process')

q = Queue()
print('a child process will start')
Process(target=f,args=(q,)).start()
sleep(.5)
print('the child process is wait put a object to Queue,main process sleep 10,then put a object to Queue')
sleep(10)
q.put('this str is from main process')

def pf(p):
    p.send(p.recv()*2)
    print('child process get object from main process and send object*2')
p1,p2 = Pipe()
p1.send(5)
print('main process send 5 to pipe')
Process(target=pf,args=(p2,)).start()
print('main process get object from pipe:')
print(p1.recv())
