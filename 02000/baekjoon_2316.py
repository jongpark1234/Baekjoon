from collections import deque
n, p = map(int, input().split())
city1 = [[0 for _ in range(n * 2)] for _ in range(n * 2)]
city2 = [[0 for _ in range(n * 2)] for _ in range(n * 2)]
graph = [[] for _ in range(2 * n)]
s, e = 1, 2
result = 0
for i in range(p):
    a, b = map(int, input().split())
    a = (a - 1) * 2 + 1
    b = (b - 1) * 2
    city1[a][b] = 1
    graph[a].append(b)
    graph[b].append(a)
    city1[b + 1][a - 1] = 1
    graph[b + 1].append(a - 1)
    graph[a - 1].append(b + 1)
for i in range(n):
    a, b = i * 2, i * 2 + 1
    city1[a][b] = 1
    graph[a].append(b)
    graph[b].append(a)
while 1:
    q = deque([s])
    prev = [-1] * (2 * n)
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if city1[x][nx] - city2[x][nx] > 0 and prev[nx] == -1:
                prev[nx] = x
                q.append(nx)
    if prev[e] == -1:
        break
    x = e
    while x != s:
        nx = prev[x]
        city2[nx][x]  +=  1
        city2[x][nx] -=  1
        x = nx
    result += 1
print(result)
