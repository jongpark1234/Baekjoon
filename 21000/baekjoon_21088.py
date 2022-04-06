from math import gcd
from sys import setrecursionlimit
setrecursionlimit(10 ** 4)
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
def isprime(num):
    numlist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    if num == 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0:
        return False
    for i in numlist:
        if num == i:
            return True
        if not millerRabin(num, i):
            return False
    return True
sieve = [False for _ in range(1000000)]
primes = []
n = int(input())
result = 0
for i in range(2, 1000):
    if sieve[i]:
        continue
    for j in range(i * i, 1000000, i):
        sieve[j] = True
for i in range(2, 1000000):
    if sieve[i]:
        continue
    primes.append(i)
Arr = list(map(int, input().split()))
for f in primes:
    length = 0
    for i in range(n):
        if Arr[i] == 1 or Arr[i] % f != 0:
            if length > 0:
                result ^= length
            length = 0
            continue
        while Arr[i] % f == 0:
            Arr[i] //= f
        length += 1
    result ^= length
for i in range(n):
    if Arr[i] == 1:
        continue
    square = -1
    is_prime = isprime(Arr[i])
    if not is_prime:
        if int(Arr[i] ** 0.5) ** 2 == Arr[i]:
            square = int(Arr[i] ** 0.5)
    if is_prime or square > 0:
        f = Arr[i] if is_prime else square
        length = 0
        for j in range(i, n):
            if Arr[j] == 1 or Arr[j] % f != 0:
                if length > 0:
                    result ^= length
                length = 0
                continue
            while Arr[j] % f == 0:
                Arr[j] //= f
            length += 1
        result ^= length
    else:
        j = i
        f = Arr[i]
        length = 0
        while j < n:
            if Arr[j] == 1:
                length = 0
                j += 1
                continue
            if Arr[j] % f != 0:
                GCD = gcd(Arr[j], f)
                if GCD == 1:
                    length = 0
                    j += 1
                    continue
                result ^= length
                while j < n:
                    if Arr[j] == 1 or Arr[j] % GCD != 0:
                        result ^= length
                        length = 0
                        break
                    while Arr[j] % GCD == 0:
                        Arr[j] //= GCD
                    length += 1
                    j += 1
            while Arr[j] % f == 0:
                Arr[j] //= f
            length += 1
            j += 1
print('First' if result else 'Second')
