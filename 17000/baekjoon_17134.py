from decimal import Decimal, Context, setcontext, MAX_PREC, MAX_EMAX
from math import isqrt
from sys import stdin
def multiply(a, b, digit = 0):
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
def sieve(n):
    if n < 3: 
        return [2] if n == 2 else []
    size = (n - 3) // 2
    isPrime = [True for _ in range(size + 1)]
    for i in range(isqrt(n - 3) // 2 + 1):
        if isPrime[i]:
            p = i + i + 3
            s = p * (i + 1) + i
            isPrime[s::p] = [False for _ in range((size - s) // p + 1)]
    return [2] + [i * 2 + 3 for i, j in enumerate(isPrime) if j]
nList = [int(stdin.readline()) for _ in range(int(stdin.readline()))]
maxNum = max(nList)
num1 = [False for _ in range(maxNum + 1)]
num2 = num1[:]
for prime in sieve(maxNum):
    num1[prime] = True
    if prime * 2 < maxNum:
        num2[prime * 2] = True
result = multiply(num1, num2)
print(*(result[i] for i in nList), sep='\n')
