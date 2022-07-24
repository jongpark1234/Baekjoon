from sys import setrecursionlimit
setrecursionlimit(10 ** 6)
def dfs(idx: int) -> int:
    if not visited1[idx]:
        visited1[idx] = True
        for i in range(len(f[idx])):
            if f[idx][i]:
                if (temp := dfs(i)) == -1:
                    return temp
                result[idx] = max(result[idx], f[idx][i] + dfs(i))
        visited2[idx] = True
    elif not visited2[idx]:
        result[idx] = -1
    return result[idx]
n, s, t = map(int, input().split())
s -= 1; t -= 1
map1 = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(2)]
map2 = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(2)]
d = [[float('inf') for _ in range(n)] for _ in range(2)]
f = [[0 for _ in range(n << 1)] for _ in range(n << 1)]
for i in range(2):
    m = int(input())
    for _ in range(m):
        a, b, l = map(int, input().split())
        a -= 1; b -= 1
        if not map1[i][a][b] or l < map1[i][a][b]:
            map1[i][a][b] = map1[i][b][a] = l
        if not map2[i][a][b] or l > map2[i][a][b]:
            map2[i][a][b] = map2[i][b][a] = l
for i in range(2):
    d[i][t] = 0
    visited1 = [False for _ in range(n)]
    for _ in range(1, n):
        minN, minI = float('inf'), -1
        for j in range(n):
            if not visited1[j] and minN > d[i][j]:
                minN, minI = d[i][j], j
        visited1[minI] = True
        for j in range(n):
            if map1[i][minI][j]:
                d[i][j] = min(d[i][j], minN + map1[i][minI][j])
for i in range(n):
    for j in range(n):
        f[i][j + n] = map2[0][i][j] if map1[0][i][j] and d[0][i] > d[0][j] else 0
        f[i + n][j] = map2[1][i][j] if map1[1][i][j] and d[1][i] > d[1][j] else 0
result = [0 for _ in range(n << 1)]
visited1 = [False for _ in range(n << 1)]
visited2 = [False for _ in range(n << 1)]
print(dfs(s))
