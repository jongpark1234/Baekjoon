from collections import deque
from math import inf
def Solve():
    c = [[0 for _ in range(v * 2 + 2)] for _ in range(v * 2 + 2)]
    d = [[0 for _ in range(v * 2 + 2)] for _ in range(v * 2 + 2)]
    f = [[0 for _ in range(v * 2 + 2)] for _ in range(v * 2 + 2)]
    graph = [[] for _ in range(v + e + 2)]
    for i in range(e):
        x, y, z = map(int, input().split())
        x = (x - 1) * 2 + 1
        y = (y - 1) * 2
        c[x][y] = 1
        d[x][y] = z
        d[y][x] = -z
        graph[x].append(y)
        graph[y].append(x)
    for i in range(v):
        x, y = i * 2, i * 2 + 1
        c[x][y] = 1
        graph[x].append(y)
        graph[y].append(x)
    cost = 0
    S = 1
    E = (v - 1) * 2
    for i in range(2):
        prev = [-1 for _ in range(v * 2)]
        dist = [inf for _ in range(v * 2)]
        inQ = [0 for _ in range(v * 2)]
        queue = deque([S])
        dist[S] = 0
        inQ[S] = 1
        while queue:
            x = queue.popleft()
            inQ[x] = 0
            for nx in graph[x]:
                if c[x][nx] - f[x][nx] > 0 and dist[nx] > dist[x] + d[x][nx]:
                    dist[nx] = dist[x] + d[x][nx]
                    prev[nx] = x
                    if inQ[nx] == 0:
                        queue.append(nx)
                        inQ[nx] = 1
        flow = inf
        x = E
        while x != S:
            nx = prev[x]
            flow = min(flow, c[nx][x] - f[nx][x])
            x = nx
        x = E
        while x != S:
            nx = prev[x]
            f[nx][x] += flow
            f[x][nx] -= flow
            cost += flow * d[nx][x]
            x = nx
    print(cost)
while True:
    try:
        v, e = map(int, input().split())
        Solve()
    except EOFError:
        break
