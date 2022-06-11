from sys import setrecursionlimit
from math import gcd
from random import randrange
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
def dfs(count, primes, prime, length, it, temp):
    if it == length:
        for _ in range(prime[1]):
            temp *= prime[0]
        for i in range(prime[1])[::-1]:
            key = temp // prime[0]
            value = count[temp] if temp in count.keys() else 0
            if key in count.keys():
                count[key] += value
            else:
                count[key] = value
            if i > 0:
                temp //= prime[0]
    else:
        if primes[it][0] == prime[0]:
            dfs(count, primes, prime, length, it + 1, temp)
        else:
            for i in range(primes[it][1] + 1):
                dfs(count, primes, prime, length, it + 1, temp)
                if i < primes[it][1]:
                    temp *= primes[it][0]
n, k = map(int, input().split())
arr = list(map(int, input().split()))
visited = [False for _ in range(n)]
result = 0
for _ in range(min(n, 20)):
    while True:
        idx = randrange(4294967295) % n
        if not visited[idx]:
            break
    visited[idx] = True
    count = {}
    for i in range(n):
        key = gcd(arr[i], arr[idx])
        if key in count.keys():
            count[key] += 1
        else:
            count[key] = 1
    factors = compress(factorize(arr[idx]))
    for i in factors:
        dfs(count, factors, i, len(factors), 0, 1)
    for i in count.items():
        if i[1] >= n - k:
            result = max(result, i[0])
print(result)
