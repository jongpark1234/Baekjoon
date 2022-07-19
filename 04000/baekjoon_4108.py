dx, dy = [-1, 0, 1, 1, 1, 0, -1, -1], [-1, -1, -1, 0, 1, 1, 1, 0]
while True:
    r, c = map(int, input().split())
    if r == c == 0:
        break
    board = [input() for _ in range(r)]
    for y in range(r):
        for x in range(c):
            if board[y][x] == '*':
                print('*', end = '')
            else:
                minesweeper = 0
                for i in range(8):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < c and 0 <= ny < r:
                        if board[ny][nx] == '*':
                            minesweeper += 1
                print(minesweeper, end='')
        print()
