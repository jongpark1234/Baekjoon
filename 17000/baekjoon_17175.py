n = int(input())
dp = [1, 1]
for i in range(2, n + 1):
    dp.append((dp[i - 1] + dp[i - 2] + 1) % 1000000007)
print(dp[-1])
