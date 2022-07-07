from collections import deque
from itertools import combinations
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
def bfs(virus):
    ret = 0
    retBoard = []
    for i in board:
        retBoard.append(i[:])
    for i in virus:
        retBoard[i[1]][i[0]] = 0
    queue = deque(virus[:])
    while queue:
        x, y, time = queue.popleft()
        for i in range(4):
            tempX, tempY = x + dx[i], y + dy[i]
            if tempX < 0 or tempX >= n or tempY < 0 or tempY >= n:
                continue
            if retBoard[tempY][tempX] == 'S':
                queue.append([tempX, tempY, time + 1])
                retBoard[tempY][tempX] = time
    for i in retBoard:
        if 'S' in i:
            return float('inf')
        for j in i:
            if type(j) == int:
                ret = max(ret, j)
    return ret
result = float('inf')
virus = []
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
for y in range(n):
    for x in range(n):
        if board[y][x] == 2:
            virus.append([x, y, 1])
for i in range(n):
    for j in range(n):
        board[i][j] = '-' if board[i][j] == 1 else 'S'
for i in list(combinations(virus, m)):
    result = min(result, bfs(i))
print(-1 if result == float('inf') else result)
