from collections import deque
m, n = map(int, input().split())
storage = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
day = 0
for i in range(n):
    for j in range(m):
        if storage[i][j] == 1:
            queue.append([i, j])
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = dx[i] + x, dy[i] + y
        if 0 <= nx < n and 0 <= ny < m and storage[nx][ny] == 0:
            storage[nx][ny] = storage[x][y] + 1
            queue.append([nx, ny])
for i in storage:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    day = max(day, max(i))
print(day - 1)
