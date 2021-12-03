from sys import stdin, setrecursionlimit
from copy import deepcopy
setrecursionlimit(10**6)
n = int(stdin.readline())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
result = 0
Max = 0
Min = 101
def search(x, y):
    if x <= -1 or y <= -1 or x >= n or y >= n:
        return False
    if Map[x][y] == 0:
        Map[x][y] = 1
        search(x + 1, y)
        search(x, y + 1)
        search(x - 1, y)
        search(x, y - 1)
        return True
    return False
for i in graph:
    Max = max(max(i), Max)
    Min = min(min(i), Min)
for i in range(Min - 1, Max):
    count = 0
    Map = deepcopy(graph)
    for j in range(n):
        for k in range(n):
            if Map[j][k] <= i:
                Map[j][k] = 1
            else:
                Map[j][k] = 0
    for j in range(n):
        for k in range(n):
            if search(j, k):
                count += 1
    result = max(result, count)
print(result)
