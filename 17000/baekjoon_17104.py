from sys import stdin
from decimal import Decimal, Context, setcontext, MAX_PREC, MAX_EMAX
MAX = 1000001
def multiply(a):
    setcontext(Context(prec = MAX_PREC, Emax = MAX_EMAX))
    digit = len(str(min(len(a), len(a)) * max(a) * max(a)))
    dec = Decimal(''.join(format(i, f'0{digit}d') for i in a)) ** 2
    total_digit = digit * (len(a) * 2 - 1)
    c = format(dec, f'0{total_digit}f')
    return [int(c[i:i + digit]) for i in range(0, total_digit, digit)]
sieve = [False for _ in range(2)] + [True for _ in range(MAX - 1)]
for i in range(2, MAX + 1):
    if sieve[i]:
        for j in range(i + i, MAX + 1, i):
            sieve[j] = False
goldbach = multiply(sieve)
for _ in range(int(input())):
    n = int(stdin.readline())
    result = goldbach[n]
    if sieve[n >> 1]:
        print((result - 1) // 2 + 1)
    else:
        print(result // 2)
