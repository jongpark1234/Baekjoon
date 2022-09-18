from heapq import *
pq = []
result = total = temp = 0
n, t, p = map(int, input().split())
k = list(map(int, input().split()))
for i in range(n):
    if t - p * i < 0:
        break
    total += k[i]
    temp += 1
    heappush(pq, -k[i])
    while total > t - p * i:
        total += heappop(pq)
        temp -= 1
    result = max(result, temp)
print(result)
