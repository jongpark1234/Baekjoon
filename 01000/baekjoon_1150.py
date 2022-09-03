from heapq import *
result = 0
n, k = map(int, input().split())
s = [int(input()) for _ in range(n)]
visited = [False for _ in range(n + 1)]
queue = [[float('inf'), 0], [float('inf'), n]]
dist, l, r = [0 for _ in range(n + 1)], [0 for _ in range(n + 1)], [0 for _ in range(n + 1)]
dist[0] = dist[n] = float('inf')
l[n], r[0] = n - 1, 1
for i in range(1, n):
    dist[i] = s[i] - s[i - 1]
    l[i], r[i] = i - 1, i + 1
    heappush(queue, [dist[i], i])
for _ in range(k):
    while True:
        d, i = heappop(queue)
        if not visited[i]:
            break
    result += d
    dist[i] = dist[l[i]] + dist[r[i]] - dist[i]
    heappush(queue, [dist[i], i])
    visited[l[i]] = visited[r[i]] = True
    l[i], r[i] = l[l[i]], r[r[i]]
    l[r[i]] = r[l[i]] = i
print(result)
