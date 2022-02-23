from sys import stdin
from math import gcd
X = 1000000007
def getExpectedValue(n, s):
    return s * getSquaredNumber(n, X - 2) % X
def getSquaredNumber(num, exp):
    if exp == 1:
        return num
    if exp % 2 == 0:
        halfnum = getSquaredNumber(num, exp // 2)
        return halfnum * halfnum % X
    else:
        return num * getSquaredNumber(num, exp - 1) % X
sum = 0
for _ in range(int(stdin.readline())):
    n, s = map(int, stdin.readline().split())
    GCD = gcd(n, s)
    n //= GCD
    s //= GCD
    sum += getExpectedValue(n, s)
    sum %= X
print(sum)