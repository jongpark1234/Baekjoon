from heapq import *
result, pq1, pq2 = [], [], []
n, l = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    heappush(pq1, a[i])
    if len(pq1) > l:
        heappush(pq2, a[i - l])
    while pq2:
        if pq1[0] == pq2[0]:
            heappop(pq1)
            heappop(pq2)
        else:
            break
    result.append(pq1[0])
print(*result)
