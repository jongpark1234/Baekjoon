from sys import stdin
n = int(stdin.readline())
graph = [[] for i in range(n + 1)]
visited = [False for i in range(n + 1)]
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
for i in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
dfs(1)
print(visited.count(True) - 1)
