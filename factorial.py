# Factorial with dynamic programming

def factorial(n :int=None) ->int:
    if not n: return None

    if n == 1: return 1

    return n * factorial(n-1)

print(factorial(10))
