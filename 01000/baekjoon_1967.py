from sys import setrecursionlimit
setrecursionlimit(10 ** 5)
def dfs(x: int, r: int) -> None:
    global last, result
    if visited[x]:
        return
    visited[x] = True
    if result < r:
        result, last = r, x
    for i, j in graph[x]:
        dfs(i, j + r)
result = last = 0
graph = [[] for _ in range(10001)]
visited = [False for _ in range(10001)]
for _ in range(int(input()) - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
dfs(1, 0)
result, visited = 0, [False for _ in range(10001)]
dfs(last, 0)
print(result)
