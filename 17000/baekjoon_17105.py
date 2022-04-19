from decimal import Decimal, Context, setcontext, MAX_PREC, MAX_EMAX
from sys import stdin
from math import *
def Sieve(limit):
    if limit < 3:
        return [[],[2]][limit == 2]
    size = (limit - 3) // 2
    primes = [True for _ in range(size + 1)]
    for i in range(isqrt(limit - 3) // 2 + 1):
        if primes[i]:
            p = i + i + 3
            s = p * (i + 1) + i
            primes[s::p] = [False for _ in range((size - s) // p + 1)]
    return [2] + [i + i + 3 for i, v in enumerate(primes) if v]
def Multiply(a, b, digit = 0):
    setcontext(Context(prec=MAX_PREC, Emax=MAX_EMAX))
    if digit == 0:
        digit = len(str(min(len(a), len(b)) * max(a) * max(b)))
    f = f'0{digit}d'
    a_dec = Decimal(''.join(format(x, f) for x in a))
    b_dec = Decimal(''.join(format(x, f) for x in b))
    c_dec = a_dec * b_dec
    total_digit = digit * (len(a) + len(b) - 1)
    c = format(c_dec, f'0{total_digit}f')
    return [int(c[i:i + digit]) for i in range(0, total_digit, digit)]
n = [int(stdin.readline()) for _ in range(int(stdin.readline()))]
p = [0 for _ in range(max(n) // 2 + 1)]
for prime in Sieve(max(n)):
    p[prime // 2] = 1
pp = [[i, i + 3][i % 2] for i in Multiply(p, p)[:max(n) // 2]]
ppp = Multiply(pp, p)
print(*((ppp[x // 2 - 1] + 2) // 6 + p[(x - 4) // 2] for x in n), sep = '\n')
