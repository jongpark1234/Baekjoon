from random import randrange
from math import gcd
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
def factorize(n):
    ret = []
    if n < 2:
        return ret
    if not n % 2:
        cnt = 0
        while not n % 2:
            cnt += 1
            n //= 2
        ret.append([2, cnt])
    if n == 1:
        return ret
    while not isprime(n):
        cnt = 0
        factor = pollardRho(n)
        while n % factor == 0:
            cnt += 1
            n //= factor
        if cnt:
            ret.append([factor, cnt])
        if n == 1:
            break
    if n != 1:
        ret.append([n, 1])
    return ret
def randomize(p, t):
    num = pow(p, t)
    phi = num // p * (p - 1)
    factors = [i for i, _ in factorize(phi)]
    while True:
        flag = True
        ret = randrange(2, num)
        if ret % p == 0:
            continue
        for i in factors:
            if pow(ret, phi // i, num) == 1:
                flag = False
                break
        if flag:
            return ret
def phi(n):
    for i, _ in factorize(n):
        n = n // i * (i - 1)
    return n
def CRT(a, b, x, y):
    return (x * b * pow(b, phi(y) - 1, y) + a * y * pow(y, phi(b) - 1, b)) % (b * y)
m, k = map(int, input().split())
for i, j in factorize(m):
    if i == 2 and k + 1 <= j - 1:
        o = (1 << (j - k)) + 1
        print(o if (1 << j) == m else CRT(o, 1 << j, 1, m // (1 << j)))
        exit(0)
    elif (i - 1) % 2 ** k == 0:
        r = i ** j
        o = pow(randomize(i, j), r // i * (i - 1) // (1 << k), r)
        print(o if r == m else CRT(o, r, 1, m // r))
        exit(0)
print(-1)
