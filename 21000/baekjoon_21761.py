from sys import stdin
from math import prod
from heapq import heappush, heappop
cards = [[] for _ in range(4)]
n, k = map(int, stdin.readline().split())
lengths = list(map(int, stdin.readline().split()))
Max = prod(lengths)
for _ in range(n):
    t, u = map(lambda x: int(x) if x.isnumeric() else x, stdin.readline().split())
    heappush(cards[ord(t) - 65], (-u, u))
for _ in range(k):
    idx = -1
    for i in range(4):
        if cards[i]:
            lengths[i] += cards[i][0][1]
            temp = prod(lengths)
            lengths[i] -= cards[i][0][1]
            if Max < temp:
                Max = temp
                idx = i
    length = heappop(cards[idx])[1]
    lengths[idx] += length
    print(chr(idx + 65), length)
