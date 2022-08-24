from sys import setrecursionlimit
setrecursionlimit(10 ** 5)
def dfs(x):
    dp[x][0] = 0
    dp[x][1] = [0, -1][x == 1]
    for i, j in graph[x]:
        dfs(i)
        for p in range(k, 0, -1):
            for q in range(1, p + 1):
                if dp[x][p - q] == -1 or dp[i][q] == -1:
                    continue
                dp[x][p] = max(dp[x][p], dp[x][p - q] + dp[i][q] + min(q, k - q + 1) * j * 2)
for i in range(int(input())):
    n, k = map(int, input().split())
    graph = [[] for _ in range(1001)]
    dp = [[-1 for _ in range(1001)] for _ in range(1001)]
    for j in range(2, n + 1):
        p, c = map(int, input().split())
        graph[p].append([j, c])
    dfs(1)
    print(f'Case {i + 1}: {dp[1][k]}')
