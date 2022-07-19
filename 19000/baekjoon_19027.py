from collections import deque
Map = [[False for _ in range(1001)] for _ in range(1001)]
dist = [[False for _ in range(1001)] for _ in range(1001)]
n, m, r, c = map(int, input().split())
for i in range(1, n + 1):
    Input = ' ' + input()
    for j in range(1, m + 1):
        if Input[j] == '@':
            Map[i][j] = True
        if Input[j] == 'A':
            x1, y1 = i, j
        if Input[j] == 'B':
            x2, y2 = i, j
result, Map[x1][y1] = False, True
dx, dy = [r, r, -r,-r, c, c, -c, -c], [c, -c, c, -c, r, -r, r, -r]
queue = deque([[x1, y1]])
while queue:
    x, y = queue.popleft()
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 1 <= nx <= n and 1 <= ny <= m:
            if Map[nx][ny] == False:
                dist[nx][ny] = not dist[x][y]
                if nx == x2 and ny == y2 and not (x == x1 and x == x2):
                    print('Bob' if dist[nx][ny] else 'Alice')
                    exit(0)
                queue.append([nx, ny])
                if not (nx == x2 and ny == y2):
                    Map[nx][ny] = True
                result = True
print('Alice' if result else 'Bob')
