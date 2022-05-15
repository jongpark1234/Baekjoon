from sys import setrecursionlimit
setrecursionlimit(10 ** 6)
def dfs(idx):
    if visited[idx]:
        return False
    if not graph[idx]:
        return True
    for i in graph[idx]:
        if dfs(i):
            return True
    return False
n, m = map(int, input().split())
visited = [False for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
s = int(input())
for i in map(int, input().split()):
    visited[i] = True
print('yes' if dfs(1) else 'Yes')
