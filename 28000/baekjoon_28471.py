from collections import deque
result = 0
dr, dc = [-1, -1, -1, 0, 0, 1, 1], [-1, 0, 1, -1, 1, -1, 1]
n = int(input())
board = [list(input()) for _ in range(n)]
for i in range(n):
    if 'F' in board[i]:
        r, c = i, board[i].index('F')
queue = deque([[r, c]])
while queue:
    r, c = queue.popleft()
    for i in range(7):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < n and 0 <= nc < n:
            if board[nr][nc] == '.':
                board[nr][nc] = '#'
                queue.append([nr, nc])
                result += 1
print(result)
