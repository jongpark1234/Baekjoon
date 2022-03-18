import heapq
Min = 0
queue = []
n = int(input())
a = list(map(int, input().split()))
x = [0 for _ in range(n)]
for i in range(n):
    heapq.heappush(queue, (a[i] - i) * -1)
    heapq.heappush(queue, (a[i] - i) * -1)
    heapq.heappop(queue)
    x[i] = heapq.heappop(queue) * -1
    heapq.heappush(queue, -x[i])
for i in range(n - 1)[::-1]:
    if x[i] > x[i + 1]:
        x[i] = x[i + 1]
for i in range(n):
    Min += abs(a[i] - x[i] - i)
print(Min)
