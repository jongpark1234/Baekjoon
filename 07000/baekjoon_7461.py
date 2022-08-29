result = [[0 for _ in range(1001)] for _ in range(1001)]
n, m = map(int, input().split())
for i in range(1, m + 1):
    result[0][i] = result[0][i - 1] + m / i
for i in range(1, n + 1):
    result[i][0] = result[i - 1][0] + n / i
    for j in range(1, m + 1):
        result[i][j] = (i * j * result[i - 1][j - 1] + (n - i) * j * result[i][j - 1] + i * (m - j) * result[i - 1][j] + m * n) / (i * m + j * n - i * j)
print(result[n][m])
