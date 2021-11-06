from collections import deque
n, m, v = map(int, input().split())
dfsvisited = [0] * (n + 1)
bfsvisited = [0] * (n + 1)
graph = [[] for i in range(n + 1)]
def dfs(v):
    print(v, end=' ')
    dfsvisited[v] = 1
    for i in graph[v]:
        if not dfsvisited[i]:
            dfs(i)
def bfs(v):
    queue = deque([v])
    bfsvisited[v] = 1
    while queue:
        popitem = queue.popleft()
        print(popitem, end= ' ')
        for i in graph[popitem]:
            if not bfsvisited[i]:
                queue.append(i)
                bfsvisited[i] = 1
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
dfs(v)
print()
bfs(v)
