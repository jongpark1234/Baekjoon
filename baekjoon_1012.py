from sys import *
setrecursionlimit(10**6)
def search(x, y):
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
    if Map[x][y] == 1:
        Map[x][y] = 0
        search(x - 1, y)
        search(x, y - 1)
        search(x + 1, y)
        search(x, y + 1)
        return True
    else:
        return False
for i in range(int(stdin.readline())):
    cnt = 0
    m, n, k = map(int, stdin.readline().split())
    Map = [[0 for i in range(m)] for j in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        Map[y][x] = 1
    for i in range(n):
        for j in range(m):
            if search(i, j):
                cnt += 1
    print(cnt)
