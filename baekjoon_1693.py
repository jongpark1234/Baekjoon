from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
n = int(stdin.readline())
s = [[] for i in range(n + 1)]
dp = [[0] * 17 for i in range(n + 1)]
visit = [False for i in range(n + 1)]
def dfs(idx):
    for i in s[idx]:
        if visit[i]:
            continue
        visit[i] = True
        dfs(i)
        for j in range(1, 17):
            m_num = 100000000
            for k in range(1, 17):
                if j != k:
                    if m_num > dp[i][k]:
                        m_num = dp[i][k]
            dp[idx][j] += m_num
    for i in range(1, 17):
        dp[idx][i] += i
    return
for i in range(n - 1):
    a, b = map(int, stdin.readline().split())
    s[a].append(b)
    s[b].append(a)
visit[1] = True
dfs(1)
print(min(dp[1][1:]))
