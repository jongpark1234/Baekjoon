MOD = 10007
dp1, dp2 = [[0 for _ in range(1002)] for _ in range(1002)], [[0 for _ in range(1002)] for _ in range(1002)]
s = ' ' + input()
result = n = len(s) - 1
for i in range(1, n):
    for j in range(n, i, -1):
        if s[i] == s[j]:
            dp2[i][j] = (dp1[i - 1][j + 1] + 1) % MOD
        dp1[i][j] = (dp1[i][j + 1] + dp1[i - 1][j] - dp1[i - 1][j + 1] + dp2[i][j] + MOD) % MOD
        result = (result + MOD + dp2[i][j] * (j - i)) % MOD
print(result % MOD)
