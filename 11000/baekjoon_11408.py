# pypy3
from collections import deque
from math import inf
n, m = map(int, input().split())
S = n + m
E = n + m + 1
c = [[False for _ in range(n + m + 2)] for _ in range(n + m + 2)]
d = [[False for _ in range(n + m + 2)] for _ in range(n + m + 2)]
f = [[False for _ in range(n + m + 2)] for _ in range(n + m + 2)]
graph = [[] for _ in range(n + m + 2)]
for i in range(n):
    numlist = list(map(int, input().split()))
    c[S][i] = 1
    graph[i].append(S)
    graph[S].append(i)
    for j in range(1, len(numlist), 2):
        w, p = numlist[j], numlist[j + 1]
        w += n - 1
        c[i][w] = 1
        d[i][w] = p
        d[w][i] = -p
        graph[i].append(w)
        graph[w].append(i)
for i in range(m):
    c[i + n][E] = 1
    graph[i + n].append(E)
    graph[E].append(i+n)
result = 0
cost = 0
while 1:
    queue = deque([S])
    prev = [-1 for _ in range(n + m + 2)]
    dist = [inf for _ in range(n + m + 2)]
    inQ = [False for _ in range(n + m + 2)]
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
    if prev[E] == -1:
        break
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
    result += 1
print(result)
print(cost)
