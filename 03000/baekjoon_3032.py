n = int(input())
dp = [[0 for _ in range(201)] for _ in range(201)]
for i, x in enumerate(map(int, input().split())):
    dp[i][i] = dp[n + i][n + i] = x & 1
for i in range(2, n + 1):
    for j in range(n << 1):
        k = i + j - 1
        if k >= n << 1:
            break
        dp[j][k] = max(dp[j][j] - dp[j + 1][k], dp[k][k] - dp[j][k - 1])
print(sum(dp[i][i] - dp[i + 1][n + i - 1] > 0 for i in range(n)))
