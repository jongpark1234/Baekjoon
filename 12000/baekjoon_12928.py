n, s = map(int, input().split())
dp = [[[False for _ in range(2001)] for _ in range(50)] for _ in range(50)]
dp[0][0][0] = True
for i in range(1, n):
    for j in range(n - 1):
        for k in range(j, s * 2 - n + 3):
            idx = 0
            while idx <= j and idx ** 2 <= k:
                dp[i][j][k] = dp[i][j][k] or dp[i - 1][j - idx][k - idx ** 2]
                idx += 1
for i in range(1, n):
    temp = s * 2 - n + 1 + i * 2 - i ** 2
    if temp < 0:
        break
    if dp[n - 1][n - i - 1][temp]:
        print(1)
        exit(0)
print(0)
