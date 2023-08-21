import heapq
pq, x = [], []
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    for _ in range(2):
        heapq.heappush(pq, -(a[i] - i))
    heapq.heappop(pq)
    x.append(-heapq.heappop(pq))
    heapq.heappush(pq, -x[i])
for i in range(n - 2, -1, -1):
    if x[i] > x[i + 1]:
        x[i] = x[i + 1]
print(sum(abs(a[i] - x[i] - i) for i in range(n)))
