from heapq import *
pq = []
n = int(input())
for i in range(n):
    heappush(pq, float(input()))
while pq:
    if len(pq) == 1:
        break
    a = heappop(pq)
    b = heappop(pq)
    heappush(pq, ((a + b) / 2))
print(pq[0])
