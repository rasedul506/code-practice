import time

def fibonacci_rec(target: int=None):
    if target == 0: return 0
    if target == 1: return 1
    return fibonacci_rec(target-1)+fibonacci_rec(target-2)

cache={}

def fibonacci_memo(target: int=None):
    if target in cache:
        return cache[target]
    if target == 0: return 0
    if target == 1: return 1
    value = fibonacci_memo(target-1)+fibonacci_memo(target-2)
    cache[target]=value
    return value

start=time.time()
print(fibonacci_rec(20))
end=time.time()
print(end-start)
print(fibonacci_memo(20))
end2=time.time()
print(end2-end)
