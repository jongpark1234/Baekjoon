MAX = 1505
s = [[0 for _ in range(MAX)] for _ in range(MAX)]
r = [[0 for _ in range(MAX)] for _ in range(2)]
crude = [[[0 for _ in range(MAX)] for _ in range(MAX)] for _ in range(6)]
result = 0
def calc(x, y):
    return s[x + k - 1][y + k - 1] - s[x - 1][y + k - 1] - s[x + k - 1][y - 1] + s[x - 1][y - 1]
m, n, k = map(int, input().split())
for i in range(1, m + 1):
    Input = [*map(int, input().split())]
    for j in range(1, n + 1):
        s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + Input[j - 1]
for i in range(k, m + 1):
    for j in range(k, n + 1):
        crude[0][i][j] = max(crude[0][i - 1][j], crude[0][i][j - 1])
        crude[0][i][j] = max(crude[0][i][j], calc(i - k + 1, j - k + 1))
for i in range(k, m + 1):
    for j in range(1, n - k + 2)[::-1]:
        crude[1][i][j] = max(crude[1][i - 1][j], crude[1][i][j + 1])
        crude[1][i][j] = max(crude[1][i][j], calc(i - k + 1, j))
for i in range(1, m - k + 2)[::-1]:
    for j in range(k, n - k + 2):
        crude[2][i][j] = max(crude[2][i + 1][j], crude[2][i][j - 1])
        crude[2][i][j] = max(crude[2][i][j], calc(i, j - k + 1))
for i in range(1, m - k + 2)[::-1]:
    for j in range(1, n - k + 2)[::-1]:
        crude[3][i][j] = max(crude[3][i + 1][j], crude[3][i][j + 1])
        crude[3][i][j] = max(crude[3][i][j], calc(i, j))
for i in range(k, m + 1):
    for j in range(1, n - k + 2):
        r[0][i] = max(r[0][i], calc(i - k + 1, j))
for i in range(k, n + 1):
    for j in range(1, m - k + 2):
        r[1][i] = max(r[1][i], calc(j, i - k + 1))
for i in range(1, m + 1):
    for j in range(i + k - 1, m + 1):
        crude[4][i][j] = max(crude[4][i][j - 1], r[0][j])
for i in range(1, n + 1):
    for j in range(i + k - 1, n + 1):
        crude[5][i][j] = max(crude[5][i][j - 1], r[1][j])
for i in range(k, m - k + 1):
    for j in range(i + k, m - k + 1):
        result = max(result, crude[4][1][i] + crude[4][i + 1][j] + crude[4][j + 1][m])
for i in range(k, n - k + 1):
    for j in range(i + k, n - k + 1):
        result = max(result, crude[5][1][i] + crude[5][i + 1][j] + crude[5][j + 1][n])
for i in range(k, m - k + 1):
    for j in range(k, n - k + 1):
        result = max(result, crude[4][1][i] + crude[2][i + 1][j] + crude[3][i + 1][j + 1])
for i in range(k, m - k + 1):
    for j in range(k, n - k + 1):
        result = max(result, crude[4][i + 1][m] + crude[0][i][j] + crude[1][i][j + 1])
for i in range(k, n - k + 1):
    for j in range(k, m - k + 1):
        result = max(result, crude[5][1][i] + crude[1][j][i + 1] + crude[3][j + 1][i + 1])
for i in range(k, n - k + 1):
    for j in range(k, m - k + 1):
        result = max(result, crude[5][i + 1][n] + crude[0][j][i] + crude[2][j + 1][i])
print(result)
