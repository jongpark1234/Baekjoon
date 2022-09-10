from sys import setrecursionlimit, stdin
setrecursionlimit(10 ** 5)
dx, dy = [1, 1, 1, 0, -1, -1, -1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]
def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return
    if banner[y][x] == 1:
        banner[y][x] = 0
        for i in range(8):
            dfs(x + dx[i], y + dy[i])
result = 0
m, n = map(int, stdin.readline().split())
banner = [list(map(int, stdin.readline().split())) for _ in range(m)]
for i in range(m):
    for j in range(n):
        if banner[i][j] == 1:
            result += 1
            dfs(j, i)
print(result)
