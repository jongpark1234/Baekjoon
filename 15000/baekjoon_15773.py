from heapq import *
pq = []
height = 0
n = int(input())
balloon = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: sum(x))
for l, d in balloon:
    height += d
    heappush(pq, -d)
    if height > l + d:
        height += heappop(pq)
print(len(pq))
