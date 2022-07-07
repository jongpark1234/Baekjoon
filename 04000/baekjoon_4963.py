from sys import setrecursionlimit
setrecursionlimit(10 ** 5)
dx, dy = [-1, 0, 1, 1, 1, 0, -1, -1], [-1, -1, -1, 0, 1, 1, 1, 0]
def dfs(x, y):
    graph[y][x] = 0
    for i in range(8):
        tempX, tempY = x + dx[i], y + dy[i]
        if 0 <= tempX < w and 0 <= tempY < h:
            if graph[tempY][tempX] == 1:
                dfs(tempX, tempY)
while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    result = 0
    graph = [list(map(int, input().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(j, i)
                result += 1
    print(result)
