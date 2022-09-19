MOD = 1000000007
dp = [[[0 for _ in range(256)] for _ in range(2)] for _ in range(251)]
dp[0][0][0] = dp[0][1][0] = 1
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        for k in range(251):
            dp[i][1][j ^ k] = (dp[i][1][j ^ k] + dp[i - j][0][k]) % MOD
            dp[i][0][k] = (dp[i][0][k] + dp[i - j][1][k]) % MOD
print((dp[n][0][0] + dp[n][1][0]) % MOD)
