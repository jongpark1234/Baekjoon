from sys import stdin, maxsize
import heapq
inf = maxsize
n = int(stdin.readline())
m = int(stdin.readline())
graph = [[] * (n + 1) for _ in range(n + 1)]
distance = [inf] * (n + 1)
for i in range(m):
    U, V, W = map(int, stdin.readline().split())
    graph[U].append((V, W))
s, e = map(int, stdin.readline().split())
def dijkstra(start):
    q = []
    heapq.heappush(q, (start, 0))
    distance[start] = 0
    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (i[0], cost))
dijkstra(s)
print(distance[e])
