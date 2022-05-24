MOD = 998244353
n, m = map(int, input().split())
link = [[False for _ in range(18)] for _ in range(18)]
cntlist = [False for _ in range(300001)]
numlist = [-1] + [0 for _ in range(300000)]
dp = [1] + [0 for _ in range(300000)]
for i in range(m):
    s, e = map(lambda x: int(x) - 1, input().split())
    link[s][e] = True
for i in range(1, 1 << n):
    cntlist[i] = True
    numlist[i] = -numlist[i - (i & -i)]
    for j in range(n):
        for k in range(n):
            if ((i >> j) & 1) and ((i >> k) & 1) and link[j][k]:
                cntlist[i] = False
for i in range(1, 1 << n):
    j = i
    while j > 0:
        if cntlist[j]:
            dp[i] = (dp[i] + [MOD - dp[i ^ j], dp[i ^ j]][numlist[j] > 0]) % MOD
        j = (j - 1) & i
print(dp[(1 << n) - 1] * (m * (MOD + 1) // 2 % MOD) % MOD)
