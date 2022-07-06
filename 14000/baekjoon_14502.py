from collections import deque
from itertools import combinations
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
def bfs(wall):
    ret = []
    for i in board:
        ret.append(i[:])
    for i in wall:
        ret[i[1]][i[0]] = 1
    queue = deque(virus[:])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            tempX, tempY = x + dx[i], y + dy[i]
            if tempX < 0 or tempX >= m or tempY < 0 or tempY >= n:
                continue
            if ret[tempY][tempX] == 0:
                queue.append([tempX, tempY])
                ret[tempY][tempX] = 2
    return ret
result = 0
virus, walls, poslist = [], [], []
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
for y in range(n):
    for x in range(m):
        if board[y][x] == 1:
            walls.append([x, y])
        elif board[y][x] == 2:
            virus.append([x, y])
obstacles = virus + walls
for y in range(n):
    for x in range(m):
        if [x, y] not in obstacles:
            poslist.append([x, y])
for i in list(combinations(poslist, 3)):
    for j in i:
        if board[j[1]][j[0]] != 0:
            continue
    result = max(result, sum([j.count(0) for j in bfs(i)]))
print(result)
