from sys import stdin
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
visited = [False for _ in range(26)]
def dfs(x, y, depth):
    global result
    visited[ord(board[y][x]) - 65] = True
    result = max(result, depth)
    for i in range(4):
        tempX, tempY = x + dx[i], y + dy[i]
        if tempX < 0 or tempY < 0 or tempX >= c or tempY >= r:
            continue
        if not visited[ord(board[tempY][tempX]) - 65]:
            visited[ord(board[tempY][tempX]) - 65] = True
            dfs(tempX, tempY, depth + 1)
            visited[ord(board[tempY][tempX]) - 65] = False
result = 0
r, c = map(int, stdin.readline().split())
board = [list(stdin.readline().rstrip()) for _ in range(r)]
dfs(0, 0, 1)
print(result)
