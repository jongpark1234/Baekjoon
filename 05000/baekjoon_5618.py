# pypy3
from math import gcd
from sys import stdin
n = int(stdin.readline())
numlist = list(map(int, stdin.readline().split()))
g = gcd(numlist[0], (gcd(numlist[1], numlist[-1])))
for i in range(1, (g // 2) + 1):
    if g % i == 0:
        print(i)
print(g)
