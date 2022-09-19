from heapq import *
result = 0
n = int(input())
pq = sorted([int(input()) for _ in range(n)])
for i in range(n - 1):
    temp = heappop(pq) + heappop(pq)
    result += temp
    heappush(pq, temp)
print(result)
