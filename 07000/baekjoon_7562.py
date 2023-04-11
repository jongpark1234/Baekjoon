from collections import deque
KNIGHT_MOVES = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
for _ in range(int(input())):
    l = int(input())
    visited = [[False for _ in range(l)] for _ in range(l)]
    queue = deque([[*map(int, input().split()), 0]])
    xe, ye = map(int, input().split())
    while queue:
        x, y, turn = queue.popleft()
        if visited[x][y] == True:
            continue
        if (x, y) == (xe, ye):
            print(turn)
            break
        turn += 1
        visited[x][y] = True
        for i, j in KNIGHT_MOVES:
            nx, ny = x + i, y + j
            if 0 <= nx < l and 0 <= ny < l:
                queue.append([nx, ny, turn])
