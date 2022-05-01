board = [[0 for _ in range(100)] for _ in range(100)]
result = 0
for _ in range(int(input())):
    w, h = map(int, input().split())
    for i in range(90 - h, 100 - h):
        for j in range(w, w + 10):
            board[i][j] = 1
for i in board:
    result += i.count(1)
print(result)
