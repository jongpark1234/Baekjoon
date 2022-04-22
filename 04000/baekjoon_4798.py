from sys import stdin, setrecursionlimit
from math import isqrt, gcd
setrecursionlimit(10 ** 5)
def extendedGCD(a, b):
    if b == 0:
        return [1, 0]
    t = extendedGCD(b, a % b)
    return [t[1], t[0] - t[1] * (a // b)]
def sieve(n):
    if n < 3: 
        return [2] if n == 2 else []
    size = (n - 3) // 2
    isp = [True for _ in range(size + 1)]
    for i in range(isqrt(n - 3) // 2 + 1):
        if isp[i]:
            p = i + i + 3
            s = p * (i + 1) + i
            isp[s::p] = [False for _ in range((size - s) // p + 1)]
    return [2] + [i + i + 3 for i, v in enumerate(isp) if v]
def power(x, y, p):
    r = 1
    x %= p
    while y:
        if y & 1:
            r = (r * x) % p
        y >>= 1
        x = x ** 2 % p
    return r
def millerRabin(n, a):
    r = 0
    d = n - 1
    while not d % 2:
        r += 1
        d //= 2
    x = power(a, d, n)
    if x == 1 or x == n - 1:
        return True
    for _ in range(r - 1):
        x = power(x, 2, n)
        if x == n - 1:
            return True
    return False
def isPrime(num):
    if num < 10000001:
        return num in primes
    if not (num & 1):
        return False
    if num % 3 == 0 or num % 5 == 0 or num % 7 == 0 or num % 11 == 0:
        return False
    for i in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if num == i:
            return True
        if not millerRabin(num, i):
            return False
    return True
T = 0
primes = sieve(10000001)
primes2 = primes[:78498]
while True:
    T += 1
    try:
        a, b, L, U = map(int, stdin.readline().split())
    except ValueError:
        break
    if gcd(a, b) != 1:
        pCnt = 0
        if L == 0 and isPrime(b):
            pCnt += 1
        elif L <= 1 and U >= 1 and isPrime(a + b):
            pCnt += 1
        print(f'Case {T}: {pCnt}')
        continue
    state = [True for _ in range(U - L + 1)]
    state[0] = isPrime(a * L + b)
    if L != U:
        state[1] = isPrime(a * L + a + b)
    for prime in primes2:
        if prime * prime > a * U + b:
            break
        if a % prime == 0:
            continue
        factor = (prime - b % prime) * extendedGCD(a, prime)[0] % prime
        if factor < 0:
            factor += prime
        n = L + factor - (L % prime)
        if n < L:
            n += prime
        if a * n + b == 0:
            n += prime
        if a * n + b == prime:
            n += prime
        while n <= U:
            state[n - L] = False
            n += prime
    print(f'Case {T}: {state.count(True)}')
