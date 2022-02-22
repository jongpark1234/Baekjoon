# pypy3
dp = [-1 for _ in range(1 << 20)]
def f(x, bit):
    if x == n:
        return 1
    if dp[bit] != -1:
        return dp[bit]
    for i in range(n):
        if not bit & (1 << i):
            dp[bit] = max(dp[bit], f(x + 1, bit | (1 << i)) * a[x][i] / 100)
    return dp[bit]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
print(f(0, 0) * 100)
