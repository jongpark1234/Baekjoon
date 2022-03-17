from math import gcd
from sys import stdin
a, b = map(int, stdin.readline().split())
c, d = map(int, stdin.readline().split())
fr = [a * d + c * b, b * d]
while gcd(max(fr), min(fr)) != 1 and fr[0] != 1 and fr[1] != 1:
    GCD = gcd(fr[0], fr[1])
    fr[0] //= GCD
    fr[1] //= GCD
print(fr[0], fr[1])
