from sys import stdin
from math import inf
from heapq import heappush, heappop
def dijkstra(adj, dist, st, flag = 0):
    dist[st] = 0
    PQ = [(dist[st], st)]
    while PQ:
        cdist, cur = heappop(PQ)
        if dist[cur] != cdist:
            continue
        for next, cost in adj[cur]:
            if flag and dist1[cur] + cost + dist2[next] == dist1[e]:
                continue
            if dist[next] > cdist + cost:
                dist[next] = cdist + cost
                heappush(PQ, (dist[next], next))
while True:
    n, m = map(int, stdin.readline().split())
    if n == m == 0:
        break
    s, e = map(int, stdin.readline().split())
    adj = [[] for _ in range(n)]
    rev = [[] for _ in range(n)]
    dist1, dist2, dist3 = [inf] * n, [inf] * n, [inf] * n
    for _ in range(m):
        a, b, c = map(int, stdin.readline().split())
        adj[a].append((b, c))
        rev[b].append((a, c))
    dijkstra(adj, dist1, s)
    dijkstra(rev, dist2, e)
    dijkstra(adj, dist3, s, 1)
    print(dist3[e] if dist3[e] != inf else -1)
