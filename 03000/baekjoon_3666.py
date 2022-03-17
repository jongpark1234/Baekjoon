from collections import deque
from math import inf
def edge(x, y, z):
    graph[x].append(y)
    graph[y].append(x)
    c[x][y] = z
def bfs():
    global level
    level = [-1 for _ in range(nm)]
    level[s] = 0
    queue = deque([s])
    while queue:
        x = queue.popleft()
        for nx in graph[x]:
            if c[x][nx] - f[x][nx] > 0 and level[nx] == -1:
                level[nx] = level[x] + 1
                queue.append(nx)
    return level[e] > 0
def dfs(x, end, fr):
    if x == end:
        return fr
    while work[x] < len(graph[x]):
        nx = graph[x][work[x]]
        if c[x][nx] - f[x][nx] > 0 and level[nx] == level[x] + 1:
            d = dfs(nx, end, min(c[x][nx] - f[x][nx], fr))
            if d > 0:
                f[x][nx] += d
                f[nx][x] -= d
                return d
        work[x] += 1
    return False
for _ in range(int(input())):
    n = int(input())
    result = 0
    nm = 2 * (n + 1)
    s = nm - 2
    e = nm - 1
    soldiers = 0
    c = [[0 for _ in range(nm)] for _ in range(nm)]
    graph = [[] for _ in range(nm)]
    enemy = [0 for _ in range(n)]
    D = list(map(int, input().split()))
    l, r = 0, sum(D) + 1
    for i in range(n):
        if D[i] > 0:
            edge(s, i, D[i])
            edge(i + n, e, 1)
            edge(i, i + n, 100000)
            soldiers += 1
    for i in range(n):
        adj = input()
        if D[i] != 0:
            for j in range(len(adj)):
                if adj[j] == 'Y':
                    if D[j] != 0:
                        edge(i, n + j, 100000)
                    else:
                        enemy[i] = 1
    while l <= r:
        mid = (l + r) // 2
        f = [[0 for _ in range(nm)] for _ in range(nm)]
        for i in range(n):
            if enemy[i] == 1:
                c[i + n][e] = mid
            if enemy[i] == 0 and D[i] > 0:
                c[i + n][e] = 1
        EV = soldiers - sum(enemy) + sum(enemy) * mid
        value = 0
        level = [-1 for _ in range(nm)]
        while bfs():
            work = [0 for _ in range(nm)]
            while True:
                fr = dfs(s, e, inf)
                if fr == 0:
                    break
                value += fr
        if value == EV:
            l = mid + 1
            result = max(result, mid)
        else:
            r = mid - 1
    print(result)
