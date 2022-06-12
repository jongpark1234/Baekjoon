from sys import stdin
from math import gcd
from random import randrange
from bisect import bisect_left, bisect_right
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
def backtrack(x, v):
    if x == len(factorlist):
        divisions.append(v)
    else:
        for _ in range(factorlist[x][1] + 1):
            backtrack(x + 1, v)
            v *= factorlist[x][0]
divisions, factorlist, Q, temp = [], [], [], 0
n = int(stdin.readline())
for i in map(int, stdin.readline().split()):
    temp += i
    Q.append(temp)
for i in range(len(Q) - 1):
    Q[i] = gcd(Q[i], Q[-1])
num = Q[-1]
Q.sort()
factors = factorize(num)
i = 0
while i < len(factors):
    e = i
    while e < len(factors) and factors[e] == factors[i]:
        e += 1
    factorlist.append([factors[i], e - i])
    i = e
backtrack(0, 1)
divisions.sort()
table = [[-1 for _ in range(111111)] for _ in range(60)]
for i in range(len(divisions)):
    for j in range(len(factorlist)):
        if divisions[i] > num // factorlist[j][0]:
            continue
        if num % (divisions[i] * factorlist[j][0]):
            continue
        table[j][i] = bisect_left(divisions, divisions[i] * factorlist[j][0])
numlist = [0 for _ in range(len(divisions))]
result = [0 for _ in range(len(divisions))]
for i in divisions:
    x = i
    idx1 = 1
    for j in range(len(factorlist)):
        cnt = 0
        while x % factorlist[j][0] == 0:
            x //= factorlist[j][0]
            cnt += 1
        idx2 = idx1
        for _ in range(1, cnt * idx2 + 1):
            numlist[idx1] = table[j][numlist[idx1 - idx2]]
            idx1 += 1
    k = bisect_right(Q, i) - bisect_left(Q, i)
    for j in range(idx1):
        result[numlist[j]] += k
for _ in range(int(stdin.readline())):
    q = int(stdin.readline())
    if num % q:
        print(-1)
        continue
    print(n + num // q - result[bisect_left(divisions, q)] * 2)
