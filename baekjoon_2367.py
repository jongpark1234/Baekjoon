from collections import deque
from math import inf
n, k, d = map(int, input().split())
v = [[0 for _ in range(n + d + 2)] for _ in range(n + d + 2)]
f = [[0 for _ in range(n + d + 2)] for _ in range(n + d + 2)]
graph = [[] for _ in range(n + d + 2)]
result = 0
s = n + d
e = s + 1
for i in range(n):
    v[s][i] = k
    graph[s].append(i)
    graph[i].append(s)
D = list(map(int, input().split()))
for i in range(d):
    v[n + i][e] = D[i]
    graph[n + i].append(e)
    graph[e].append(n + i)
for i in range(n):
    foodNumber = list(map(int, input().split()))
    for j in foodNumber[1:]:
        v[i][j - 1 + n] = 1
        graph[i].append(j - 1 + n)
        graph[j - 1 + n].append(i)
while True:
    q = deque([s])
    prev = [-1 for _ in range(n + d + 2)]
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if v[x][nx] - f[x][nx] > 0 and prev[nx] == -1:
                prev[nx] = x
                q.append(nx)
    if prev[e] == -1:
        break
    dish = inf
    x = e
    while x != s:
        nx = prev[x]
        dish = min(dish, v[nx][x] - f[nx][x])
        x = nx
    x = e
    while x != s:
        nx = prev[x]
        f[nx][x] += dish
        f[x][nx] -= dish
        x = nx
    result += dish
print(result)
