MAX = 2000
a = [0 for _ in range(MAX + 1)]
Sum = [0 for _ in range(MAX + 1)]
dp = [[0 for _ in range(MAX + 1)] for _ in range(MAX + 1)]
n = int(input())
for i in range(1, n + 1):
    a[n - i + 1] = int(input())
for i in range(1, n + 1):
    Sum[i] = Sum[i - 1] + a[i]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = max(dp[i][j], dp[i][j - 1])
        if i >= j * 2 - 1:
            dp[i][j] = max(dp[i][j], Sum[i] - dp[i - (j * 2 - 1)][j * 2 - 1])
        if i >= j * 2:
            dp[i][j] = max(dp[i][j], Sum[i] - dp[i - j * 2][j * 2])
print(dp[n][1])
