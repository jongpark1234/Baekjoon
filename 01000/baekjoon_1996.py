dx, dy = [-1, 0, 1, 1, 1, 0, -1, -1], [-1, -1, -1, 0, 1, 1, 1, 0]
n = int(input())
board = [input() for _ in range(n)]
for y in range(n):
    for x in range(n):
        if board[y][x].isdecimal():
            print('*', end = '')
        else:
            minesweeper = 0
            for i in range(8):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if board[ny][nx].isdecimal():
                        minesweeper += int(board[ny][nx])
            print('M' if minesweeper > 9 else minesweeper, end='')
    print()
