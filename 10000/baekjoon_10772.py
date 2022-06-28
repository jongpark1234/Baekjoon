result = [[0 for _ in range(251)] for _ in range(251)]
n = int(input())
k = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        result[i][j] = 1 if j in [1, i] else result[i - 1][j - 1] + result[i - j][j]
print(result[n][k])
