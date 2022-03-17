cost = [[0 for _ in range(101)] for _ in range(101)]
dp = [[0 for _ in range(101)] for _ in range(101)]
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    cost[a][b] = cost[b][a] = 1
for i in range(1, 101):
    for j in range(1, i + 1)[::-1]:
        for k in range(j, i):
            dp[j][i] = max(dp[j][i], dp[j][k] + dp[k][i] + cost[i][j])
print(dp[1][100])
