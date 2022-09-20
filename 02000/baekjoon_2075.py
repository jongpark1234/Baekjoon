from heapq import *
pq = []
n = int(input())
for _ in range(n):
    for i in map(int, input().split()):
        if len(pq) < n:
            heappush(pq, i)
        else:
            if pq[0] < i:
                heappop(pq)
                heappush(pq, i)
print(pq[0])
