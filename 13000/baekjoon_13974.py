dp = [[0 for _ in range(5100)] for _ in range(5100)]
K = [[0 for _ in range(5100)] for _ in range(5100)]
def solve(n):
    s = [0]
    v = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        s.append(s[i - 1] + v[i])
    for i in range(1, n + 1):
        K[i - 1][i] = i
        dp[i - 1][i] = 0
    for i in range(2, n + 1):
        for j in range(n - i + 1):
            k = j + i
            dp[j][k] = 1000000007
            for l in range(K[j][k - 1], K[j + 1][k] + 1):
                now = dp[j][l] + dp[l][k] + s[k] - s[j]
                if dp[j][k] > now:
                    dp[j][k] = now
                    K[j][k] = l
    print(dp[0][n])
for i in range(int(input())):
    solve(int(input()))
