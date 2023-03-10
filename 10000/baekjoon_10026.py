from sys import setrecursionlimit
from copy import deepcopy
setrecursionlimit(10 ** 5)
def dfs(graph, x, y, color, colorblind):
    if graph[y][x] == 'N':
        return
    if color != graph[y][x]:
        if colorblind:
            if not (color in 'RG' and graph[y][x] in 'RG'):
                return
        else:
            return
    graph[y][x] = 'N'
    if x > 0:
        dfs(graph, x - 1, y, color, colorblind)
    if y > 0:
        dfs(graph, x, y - 1, color, colorblind)
    if x < n - 1:
        dfs(graph, x + 1, y, color, colorblind)
    if y < n - 1:
        dfs(graph, x, y + 1, color, colorblind)
result1 = result2 = 0
n = int(input())
graph1 = [list(input()) for _ in range(n)]
graph2 = deepcopy(graph1)
for i in range(n):
    for j in range(n):
        if graph1[i][j] != 'N':
            result1 += 1
            dfs(graph1, j, i, graph1[i][j], False)
for i in range(n):
    for j in range(n):
        if graph2[i][j] != 'N':
            result2 += 1
            dfs(graph2, j, i, graph2[i][j], True)
print(result1, result2)
