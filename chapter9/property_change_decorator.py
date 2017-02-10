#!/usr/bin/env python
# encoding: utf-8

import time
import logging
from random import randint

def timeout(timeout):
    t=[timeout]
    def decorator(func):
        def settimeout(s):
            t[0] = s
        def wrapper(*args,**kwargs):
            start = time.time()
            res = func(*args,**kwargs)
            used = time.time() - start
            if used > t[0]:
                logging.warning('%s:%s>%s'%(func.__name__,used,t[0]))
            return res
        print('init wrapper')
        wrapper.settimeout=settimeout
        return wrapper
    return decorator

@timeout(1.5)
def f():
    print('in test')
    while randint(0,1):
        time.sleep(0.5)

for _ in range(30):
    f()

f.settimeout(1)

for _ in range(30):
    f()
