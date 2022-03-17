# pypy3
INF = 100000000
dp = [[-1 for _ in range(1 << 20)] for _ in range(21)]
def f(x, bit):
    if x == n:
        return 0
    if dp[x][bit] != -1:
        return dp[x][bit]
    dp[x][bit] = INF
    for i in range(n):
        if not bit & (1 << i):
            dp[x][bit] = min(dp[x][bit], f(x + 1, bit | (1 << i)) + a[x][i])
    return dp[x][bit]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
print(f(0, 0))
