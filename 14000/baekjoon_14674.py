from decimal import *
getcontext().prec = 99
n, k = map(int, input().split())
games = []
for _ in range(n):
    i, c, h = map(int, input().split())
    games.append([i, c, Decimal(h) / Decimal(c)])
for i in sorted(games, key = lambda x: (-x[2], x[1], x[0]))[:k]:
    print(i[0])
