from sys import stdin
n = int(stdin.readline())
m = int(stdin.readline())
snail = [[0] * n for i in range(n)]
num = n ** 2
row = n; col = n
i = -1; j = 0
dir = 1
while num != 0:
    for _ in range(row):
        i += dir
        snail[i][j] = num
        num -= 1
    row -= 1
    col -= 1
    for _ in range(col):
        j += dir
        snail[i][j] = num
        num -= 1
    dir *= -1
for i in range(n):
    for j in range(n):
        print(snail[i][j], end=' ')
        if snail[i][j] == m:
            pos = f'{i + 1} {j + 1}'
    print()
print(pos)
