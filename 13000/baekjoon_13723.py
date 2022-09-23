from math import prod
from random import randrange
from math import gcd
def primetest(n):
    def verify(a, n, s):
        if a >= n:
            a %= n
        if a < 2:
            return True
        d = n >> s
        x = pow(a, d, n)
        if x == n - 1:
            return True
        if x == 1: 
            return True
        for _ in range(s):
            x = x * x % n
            if x == 1:
                return False
            if x == n - 1:
                return True
        return False
    if n == 2:
        return True
    if n < 2 or not n & 1:
        return False
    d = n >> 1
    r = 1
    while not d & 1:
        d >>= 1
        r += 1
    numlist = [2, 7, 61] if n < 4759123141 else [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
    return all(verify(i, n, r) for i in numlist)
def factorize(n):
    def pollard_rho(n):
        x = randrange(1, n)
        c = randrange(1, n)
        y, g = x, 1
        while g == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            g = gcd(abs(x - y), n)
        if g == n:
            return pollard_rho(n)
        return g
    if n == 1:
        return []
    if not n & 1:
        return [2] + factorize(n // 2)
    if primetest(n):
        return [n]
    f = pollard_rho(n)
    return factorize(f) + factorize(n // f)
n = int(input())
result = {}
for i in range(2, n + 1):
    for i in factorize(i):
        result[i] = result.get(i, 0) + 1
print(prod(map(lambda x: (x << 1) + 1, result.values())))
