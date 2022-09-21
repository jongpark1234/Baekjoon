from heapq import *
n, m = map(int, input().split())
pq = list(map(int, input().split()))
heapify(pq)
for _ in range(m):
    temp = heappop(pq) + heappop(pq)
    for _ in range(2):
        heappush(pq, temp)
print(sum(pq))
