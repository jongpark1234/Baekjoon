x = [0 for _ in range(5001)]
dp = [x[:] for _ in range(1001)]
n, m = map(int, input().split())
for i in map(int, input().split()):
    for j in range(i, m + 1):
        x[j] += 1
for i in range(1, n + 1):
    for j in range(1, m + 1):
        for k in range(min((j + i - 1) // i, j) + 1):
            dp[i][j] = max(dp[i][j], dp[i - 1][j - k] + x[k])
print(dp[n][m] / n)
