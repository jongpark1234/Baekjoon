dp = [0, 1]
for i in range(2, 92):
    dp.append(dp[i - 2] + dp[i - 1])
print(dp[int(input())])
