n = int(input())
dp = [0, 1, 0, 1, 1, 1] + [0 for _ in range(n - 5)]
for i in range(6, n + 1):
    dp[i] = 0
    if dp[i - 1] == 0:
        dp[i] = 1
    if dp[i - 3] == 0:
        dp[i] = 1
    if dp[i - 4] == 0:
        dp[i] = 1
if dp[n] == 1:
    print('SK')
else:
    print('CY')
