from random import randrange
from math import gcd
from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)
n = int(stdin.readline())
answer = []
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
def pollardRho(num):
    if isprime(num):
        return num
    if num == 1:
        return 1
    if num % 2 == 0:
        return 2
    x = randrange(2, num)
    y = x
    c = randrange(1, num)
    d = 1
    while d == 1:
        x = ((x * x % num) + c + num) % num
        for _ in range(2):
            y = ((y * y % num) + c + num) % num
        d = gcd(abs(x - y), num)
        if d == num:
            return pollardRho(num)
    if isprime(d):
        return d
    else:
        return pollardRho(d)
while n > 1:
    factor = pollardRho(n)
    answer.append(factor)
    n //= factor
print('\n'.join(map(str, sorted(answer))))
