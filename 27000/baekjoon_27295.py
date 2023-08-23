from sys import stdin
from math import gcd
n, b = map(int, input().split())
xlist, ylist = [], []
for _ in range(n):
    x, y = map(int, stdin.readline().split())
    xlist.append(x)
    ylist.append(y)
if sum(xlist) == 0:
    print('EZPZ')
else:
    temp = sum(ylist) - b * n
    q, r = divmod(temp, sum(xlist))
    g = gcd(temp, sum(xlist))
    d, m = sum(xlist) // g, temp // g
    print(f'{"-" if (m < 0) ^ (d < 0) else""}{abs(m)}/{abs(d)}' if r else q)
