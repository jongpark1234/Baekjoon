result = 0
flag = False
multiply = [[[0 for _ in range(1004)] for _ in range(1004)] for _ in range(2)]
sumA = [[[0 for _ in range(1001)] for _ in range(1001)] for _ in range(2)]
sumB = [0, 0]
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(r)]
for i in range(r):
    for j in range(c):
        if b[0][0] != b[i][j]:
            flag = True
            x, y = j, i
if flag:
    for i in range(n):
        for j in range(m):
            for k in range(2):
                multiply[k][i][j] = i + j if k else 1
    for i in range(2):
        for j in range(n):
            for k in range(m):
                sumA[i][j + 1][k + 1] = sumA[i][j + 1][k] + sumA[i][j][k + 1] - sumA[i][j][k] + multiply[i][j][k] * a[j][k]
        for j in range(r):
            for k in range(c):
                sumB[i] += multiply[i][j][k] * b[j][k]
    for i in range(n - r + 1):
        for j in range(m - c + 1):
            if a[i][j] != a[i + y][j + x]:
                temp = r * c
                t = [sumA[k][i + r][j + c] - sumA[k][i][j + c] - sumA[k][i + r][j] + sumA[k][i][j] for k in range(2)]
                if (a[i + y][j + x] * temp - a[i][j] * temp) * (sumB[0] - b[y][x] * temp) == (b[y][x] * temp - b[0][0] * temp) * (t[0] - a[i + y][j + x] * temp):
                    if temp:
                        temp *= (r + c - 2) >> 1
                        if (a[i + y][j + x] * temp - a[i][j] * temp) * (sumB[1] - b[y][x] * temp) == (b[y][x] * temp - b[0][0] * temp) * ((t[1] - (i + j) * t[0]) - a[i + y][j + x] * temp):
                            result += 1
    print(result)
else:
    print((n - r + 1) * (m - c + 1))
