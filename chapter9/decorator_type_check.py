#!/usr/bin/env python
# encoding: utf-8

from inspect import signature

def typeassert(*ty_args,**ty_kwargs):
    def typedecorator(func):
        sig = signature(func)
        typedict = sig.bind_partial(*ty_args,**ty_kwargs).arguments
        def warp(*args,**kwargs):
            for name,obj in sig.bind(*args,**kwargs).arguments.items():
                if name in typedict:
                    if not isinstance(obj,typedict[name]):
                        raise TypeError('%s must be %s'%(name,typedict[name]))
            return func(*args,**kwargs)
        return warp
    return typedecorator

@typeassert(int,c=int,d=str)
def f(a,b,c=7,d='a'):
    print(a,b,c,d)

f(1,'d',c=8,d='abc')

f(1,'d',c=8,d=10)
