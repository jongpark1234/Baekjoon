from sys import stdin, setrecursionlimit
from math import gcd, sqrt
from random import randrange
from bisect import bisect_left
setrecursionlimit(10 ** 5)
def millerRabin(n, a):
    r = 0
    d = n - 1
    while not d % 2:
        r += 1
        d //= 2
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    for _ in range(r - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True
    return False
def isprime(num):
    numlist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
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
def factorize(num):
    numlist = []
    while num > 1:
        factor = pollardRho(num)
        numlist.append(factor)
        num //= factor
    return sorted(numlist)
def compress(l):
    Dict = {}
    for i in l:
        if i in Dict.keys():
            Dict[i] += 1
        else:
            Dict[i] = 1
    return list(Dict.items())
def dfs(d, c):
    if d == len(v):
        div.append(c)
        return
    t = 1
    for _ in range(v[d][1] + 1):
        dfs(d + 1, c * t)
        t *= v[d][0]
while True:
    n = int(stdin.readline())
    if n == 0:
        break
    if isprime(n):
        print(n + 2)
        continue
    result = n + 2
    v, div = compress(factorize(n)), []
    dfs(0, 1)
    div.sort()
    for i in range(len(div)):
        idx = bisect_left(div, int(sqrt(div[i])))
        for j in range(idx - 3, idx + 4):
            if j < 0 or j >= len(div):
                continue
            if div[i] % div[j]:
                continue
            result = min(result, n // div[i] + div[i] // div[j] + div[j])
    print(result)
