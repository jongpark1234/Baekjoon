from heapq import *
pq = []
n, k = map(int, input().split())
v = list(map(int, input().split()))
for i in range(k):
    heappush(pq, v[i])
for i in range(n - k):
    heappush(pq, v[i + k])
    v[i] = heappop(pq)
result = v[:n - k]
while pq:
    result.append(heappop(pq))
print(*result)
