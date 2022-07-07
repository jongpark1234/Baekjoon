from collections import deque
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
queue = deque([[0, 0]])
while queue:
    x, y = queue.popleft()
    for i in range(4):
        tempX, tempY = x + dx[i], y + dy[i]
        if 0 <= tempX < m and 0 <= tempY < n:
            if graph[tempY][tempX] == 1:
                graph[tempY][tempX] = graph[y][x] + 1
                queue.append([tempX, tempY])
print(graph[-1][-1])
