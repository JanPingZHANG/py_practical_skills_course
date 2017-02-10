from functools import wraps

def comn(func):
    cache = {}
    @wraps(func)
    def warp(*args):
        if args in cache:
            return cache[args]
        cache[args] = func(*args)
        return cache[args]
    return warp

def fabonicc(n):
    if n <= 1 :
        return n
    return fabonicc(n-1) + fabonicc(n-2)

fabonicc=comn(fabonicc)
print(fabonicc(55))

@comn
def climb(n,steps):
    count = 0
    if n==0:
        count = 1
    elif n>0:
        for step in steps:
            count += climb(n-step,steps)
    return count

print(climb(100,(1,2,3)))
print (climb.__name__)
