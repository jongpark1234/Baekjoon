from sys import setrecursionlimit, stdin
setrecursionlimit(10 ** 5)
def dfs(u: int, v: int) -> None:
    global result
    for i in graph[u]:
        if i == v:
            continue
        dfs(i, u)
        for j in range(16):
            poslist[u][j] += poslist[i][j]
    for i in range(16):
        if poslist[u][i] >= 2:
            pri[u] = i + 1
        elif poslist[u][i] == 1 and pri[u] == i:
            pri[u] += 1
    poslist[u][pri[u]] = 1
    for i in range(pri[u]):
        poslist[u][i] = 0
    result = max(result, pri[u])
result = 0
n = int(input())
graph = [[] for _ in range(n + 1)]
poslist = [[0 for _ in range(16)] for _ in range(n + 1)]
pri = [0 for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(1, 0)
print(result)
