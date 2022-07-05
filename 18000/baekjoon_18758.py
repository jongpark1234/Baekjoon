from sys import stdin
def ctz(x):
    return len(bin(x)[2:].split('1')[-1])
MOD = 1000000007
n, m, c = map(int, input().split())
graph = [[False for _ in range(36)] for _ in range(36)]
numlist = [[0 for _ in range(36)] for _ in range(1 << 18)]
dp1 = [0 for _ in range(1 << 18)]
dp2 = dp1[:]
result = [1]
t = n + (n & 1) >> 1
for i in range(m):
    u, v = map(lambda x: int(x) - 1, stdin.readline().split())
    graph[u][v] = graph[v][u] = True
for i in range(1 << t):
    if (i & -i) == i:
        temp = ctz(i)
        numlist[i][temp << 1] = numlist[i][(temp << 1) + 1] = dp1[i] = True
        continue
    for j in range(t):
        if not ((i >> j) & 1):
            continue
        for k in range(2):
            temp = j << 1 | k
            for l in range(n):
                if graph[temp ^ 1][l]:
                    numlist[i][temp] = (numlist[i][temp] + c * numlist[i - (1 << j)][l]) % MOD
            dp1[i] = (dp1[i] + numlist[i][temp]) % MOD
    dp1[i] = dp1[i] * (MOD + 1 >> 1) % MOD
for i in range(1, t + 1):
    g = [[0 for _ in range(36)] for _ in range(1 << i)]
    for j in range(1, 1 << i):
        if (j & -j) == j:
            temp = ctz(j)
            if temp == i - 1:
                g[j][temp << 1] = c
                if graph[temp << 1][(temp << 1) + 1]:
                    dp2[j] = c
            continue
        for k in range(i):
            if not ((j >> k) & 1):
                continue
            for l in range(2):
                temp = k << 1 | l
                for m in range(i << 1):
                    if graph[temp ^ 1][m]:
                        g[j][temp] = (g[j][temp] + c * g[j - (1 << k)][m]) % MOD
                if graph[temp][(i << 1) - 1]:
                    dp2[j] = (dp2[j] + g[j][temp]) % MOD
for i in range(1, 1 << t):
    result.append(0)
    j = i - (i & -i)
    while True:
        result[i] = (result[i] + (dp1[i - j] + dp2[i - j]) * result[j]) % MOD
        if not j:
            break
        j = (j - 1) & (i - (i & -i))
print(result[-1])
