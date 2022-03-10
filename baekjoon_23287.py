from random import randrange
from math import gcd
from sys import setrecursionlimit
setrecursionlimit(10 ** 6)
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
class Gauss:
    def __init__(self, r, n):
        self.r = r
        self.n = n
    def norm(self):
        return self.r ** 2 + self.n ** 2
    def __floordiv__(a, b): # define a // b
        def cal(a, b):
            ret = a % b
            if ret < 0:
                ret += b
            if ret * 2 > b:
                ret -= b
            return (a - ret) // b
        a1, a2 = a.r, a.n
        b1, b2 = b.r, b.n
        n = b.norm()
        return Gauss(cal(a1 * b1 + a2 * b2, n), cal(a2 * b1 - a1 * b2, n))
    def __mod__(a, b): # define a % b
        a1, a2 = a.r, a.n
        b1, b2 = b.r, b.n
        q = a // b
        q1, q2 = q.r, q.n
        return Gauss(a1 - q1 * b1 + q2 * b2, a2 - q1 * b2 - q2 * b1)
    def GCD(a, b):
        while b.r or b.n:
            a, b = b, a % b
        return a
def sumTwoSquare1(n):
    if n == 2:
        return [1, 1]
    k = n // 4
    j = 2
    while True:
        a = power(j, k, n)
        if a ** 2 % n == n - 1:
            break
        j += 1
    uc = Gauss.GCD(Gauss(n, 0), Gauss(a, 1))
    return [abs(uc.r), abs(uc.n)]
def sumTwoSquare2(n):
    s = 1
    primes = set()
    for i in factorize(n):
        if i in primes:
            s *= i
            primes.remove(i)
        else:
            primes.add(i)
    if not primes:
        return [s, 0]
    for i in primes:
        if i % 4 == 3:
            return 'E'
    a, b = s, 0
    for i in primes:
        c, d = sumTwoSquare1(i)
        a, b = a * c + b * d, a * d - b * c
    return [abs(a), abs(b)]
def sumSquare(n):
    result = 0
    if n == 0:
        return []
    if n % 4 == 0: # legendre
        while n % 4 == 0:
            n //= 4
            result += 1
        return list(map(lambda x: x << result, sumSquare(n)))
    if n % 8 == 7:
        return sumSquare(n - 1) + [1]
    ss = sumTwoSquare2(n)
    if ss != 'E':
        res = []
        a, b = ss
        if a:
            res.append(a)
        if b:
            res.append(b)
        return res
    i = 2 # fermat
    if n % 4 == 3:
        i = 1
    while True:
        ab = sumTwoSquare2(n - i ** 2)
        if ab != 'E':
            return list(ab) + [i]
        i += 2
squares = sumSquare(int(input()))
print(*sorted(squares), '0 ' * (4 - len(squares)))
