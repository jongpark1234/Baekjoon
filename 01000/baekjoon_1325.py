from sys import stdin
from collections import deque
def bfs(x):
    ret = 1
    visited = [0 for _ in range(n + 1)]
    visited[x] = True
    q = deque([x])
    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i] == False:
                visited[i] = True
                ret += 1
                q.append(i)
    return ret
n, m = map(int, input().split())
Max = 0
graph = [[] for _ in range(n + 1)]
result = []
for i in range(m):
    a, b = map(int, stdin.readline().split())
    graph[b].append(a)
for i in range(1, n + 1):
    temp = bfs(i)
    if Max == temp:
        result.append(i)
    elif Max < temp:
        Max = temp
        result = [i]
print(*result)
