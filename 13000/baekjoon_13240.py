n, m = map(int, input().split())
for i in range(n):
    board = '.*' if i & 1 else '*.'
    for j in range(m):
        print(board[j & 1], end='')
    print()
