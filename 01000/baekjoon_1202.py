from heapq import *
pq = []
n, k = map(int, input().split())
jewel = sorted([tuple(map(int, input().split())) for _ in range(n)])
c = sorted([int(input()) for _ in range(k)])
idx = result = 0
for i in range(k):
    while idx < n and jewel[idx][0] <= c[i]:
        heappush(pq, -jewel[idx][1])
        idx += 1
    if pq:
        result -= heappop(pq)
print(result)
