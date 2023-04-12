from collections import deque
result = -1
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
visited = [[[0 for _ in range(1 << 6)] for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == '0':
            visited[i][j][0] = 1
            queue = deque([(i, j, 0)])
            break
    else:
        continue
    break
while queue:
    x, y, z = queue.popleft()
    if board[x][y] == '1':
        result = visited[x][y][z] - 1
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][z] == False and board[nx][ny] != '#':
            if board[nx][ny] in 'abcdef':
                nz = z | (1 << (ord(board[nx][ny]) - ord('a')))
                if visited[nx][ny][nz] == 0:
                    visited[nx][ny][nz] = visited[x][y][z] + 1
                    queue.append((nx, ny, nz))
            elif board[nx][ny] in 'ABCDEF':
                if z & (1 << (ord(board[nx][ny]) - ord('A'))):
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    queue.append((nx, ny, z))
            else:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))
print(result)
