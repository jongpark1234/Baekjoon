# pypy3
from collections import deque
m, n, h = map(int, input().split())
storage = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
queue = deque([])
dx, dy, dz = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]
day = 0
for z in range(h):
    for y in range(n):
        for x in range(m):
            if storage[z][y][x] == 1:
                queue.append([z, y, x])
while queue:
    z, y, x = queue.popleft()
    for i in range(6):
        nx, ny, nz = dx[i] + x, dy[i] + y, dz[i] + z
        if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and storage[nz][ny][nx] == 0:
            storage[nz][ny][nx] = storage[z][y][x] + 1
            queue.append([nz, ny, nx])
for i in storage:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        day = max(day, max(j))
print(day - 1)
