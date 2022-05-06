from sys import stdin
from math import sqrt
MAX = 1e18
n, h, a, b = map(int, stdin.readline().split())
x, y = [], []
for i in range(n):
    Input = [*map(int, stdin.readline().split())]
    x.append(Input[0])
    y.append(Input[1])
cost = [a * (h - y[0])] + [MAX for _ in range(n - 1)]
for i in range(n):
    Min = 0
    Max = (h - y[i]) * 2
    for j in range(i + 1, n):
        d = x[j] - x[i]
        height = h - y[j]
        if d > Max:
            break
        if height * 2 <= d:
            Min = max(Min, d * 2 + height * 2 - sqrt(d * height * 8))
        Max = min(Max, d * 2 + height * 2 + sqrt(d * height * 8))
        if Min > Max:
            break
        if d >= Min and d <= Max:
            cost[j] = min(cost[j], cost[i] + a * height + b * d ** 2)
print('impossible' if cost[n - 1] == MAX else cost[n - 1])
