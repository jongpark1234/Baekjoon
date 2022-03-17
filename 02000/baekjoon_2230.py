from sys import stdin
from math import inf
n, m = map(int, stdin.readline().split())
a = sorted([int(stdin.readline()) for _ in range(n)])
distance = inf
l, r = 0, 1
while l < n and r < n:
    temp = a[r] - a[l]
    if temp == m:
        print(m)
        exit(0)
    if temp < m:
        r += 1
        continue
    l += 1
    distance = min(temp, distance)
print(distance)
