from heapq import *
pq = []
level = 0
n = int(input())
gold = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[1])
for t, h in gold:
    level += t
    heappush(pq, -t)
    if level > h:
        level += heappop(pq)
print(len(pq))
