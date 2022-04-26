from collections import deque
board = [[' ' for _ in range(7)] for _ in range(7)]
copiedBoard = [[' ' for _ in range(7)] for _ in range(7)]
def parsing(top, mid, bottom):
    temp = 0
    if top[1] == '|':
        temp += 1000
    if mid[0] == '-':
        temp += 100
    if mid[2] == '-':
        temp += 10
    if bottom[1] == '|':
        temp += 1
    ret = str(temp)
    return (4 - len(ret)) * '0' + ret
def inserting(row, col, p):
    r1, c1, r2, c2 = R1, C1, R2, C2
    visited = [[False for _ in range(7)] for _ in range(7)]
    for i in range(7):
        for j in range(7):
            copiedBoard[i][j] = board[i][j]
    if row == 0:
        for i in range(1, 7)[::-1]:
            copiedBoard[i][col] = copiedBoard[i - 1][col]
        copiedBoard[0][col] = p
        if r1 == 6 and c1 == col:
            r1 = 0
        elif c1 == col:
            r1 += 1
        if r2 == 6 and c2 == col:
            return False
        elif c2 == col:
            r2 += 1
    if row == 6:
        for i in range(6):
            copiedBoard[i][col] = copiedBoard[i + 1][col]
        copiedBoard[6][col] = p
        if r1 == 0 and c1 == col:
            r1 = 6
        elif c1 == col:
            r1 -= 1
        if r2 == 0 and c2 == col:
            return False
        elif c2 == col:
            r2 -= 1
    if col == 0:
        for i in range(1, 7)[::-1]:
            copiedBoard[row][i] = copiedBoard[row][i - 1]
        copiedBoard[row][0] = p
        if r1 == row and c1 == 6:
            c1 = 0
        elif r1 == row:
            c1 += 1
        if r2 == row and c2 == 6:
            return False
        elif r2 == row:
            c2 += 1
    if col == 6:
        for i in range(6):
            copiedBoard[row][i] = copiedBoard[row][i + 1]
        copiedBoard[row][6] = p
        if r1 == row and c1 == 0:
            c1 = 6
        elif r1 == row:
            c1 -= 1
        if r2 == row and c2 == 0:
            return False
        elif r2 == row:
            c2 -= 1
    result = False
    queue = deque([[r1, c1]])
    visited[r1][c1] = True
    while queue:
        R = queue[0][0]
        C = queue[0][1]
        queue.popleft()
        if R == r2 and C == c2:
            result = True
            break
        else:
            if copiedBoard[R][C][0] == '1' and R > 0 and copiedBoard[R - 1][C][3] == '1' and visited[R - 1][C] == False:
                queue.append([R -1 , C])
                visited[R - 1][C] = True
            if copiedBoard[R][C][3] == '1' and R < 6 and copiedBoard[R + 1][C][0] == '1' and visited[R + 1][C] == False:
                queue.append([R + 1, C])
                visited[R + 1][C] = True
            if copiedBoard[R][C][1] == '1' and C > 0 and copiedBoard[R][C - 1][2] == '1' and visited[R][C - 1] == False:
                queue.append([R, C - 1])
                visited[R][C - 1] = True
            if copiedBoard[R][C][2] == '1' and C < 6 and copiedBoard[R][C + 1][1] == '1' and visited[R][C + 1] == False:
                queue.append([R, C + 1])
                visited[R][C + 1] = True
    return result
while True:
    R1, C1, R2, C2 = map(int, input().split())
    if R1 == C1 == R2 == C2 == 0:
        break
    input()
    R1 -= 1
    C1 -= 1
    R2 -= 1
    C2 -= 1
    for i in range(7):
        top = input().split()
        mid = input().split()
        bottom = input().split()
        input()
        for j in range(7):
            board[i][j] = parsing(top[j], mid[j], bottom[j])
    piece = parsing(input(), input(), input())
    result = False
    for _ in range(4):
        temp = str((piece[2] == '1') * 1000 + (piece[0] == '1') * 100 + (piece[3] == '1') * 10 + (piece[1] == '1'))
        piece = (4 - len(temp)) * '0' + temp
        for i in range(3):
            result = inserting(0, i * 2 + 1, piece)
            if result:
                break
            result = inserting(6, i * 2 + 1, piece)
            if result:
                break
            result = inserting(i * 2 + 1, 0, piece)
            if result:
                break
            result = inserting(i * 2 + 1, 6, piece)
            if result:
                break
        if result:
            break
    print('You can win in one move.' if result else 'Bad luck!')
    input()
