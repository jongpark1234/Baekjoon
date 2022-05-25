MOD = 1000000007
result = 0
check = [0 for _ in range(2001)]
o = [[[0 for _ in range(2)] for _ in range(2001)] for _ in range(2001)]
w = [1]
def dfs(x, l, n):
    ret = 0
    visited[x] = 1
    if x == n - 1:
        return True
    for i in range(check[x]):
        if o[x][i][1] < l or visited[o[x][i][0]]:
            continue
        else:
            ret |= dfs(o[x][i][0], l, n)
    return ret
for i in range(1, 2001):
    w.append(w[i - 1] * 3 % MOD)
n, m = map(int, input().split())
for i in range(m):
    a, b = map(int, input().split())
    o[a][check[a]][0] = b
    o[a][check[a]][1] = i
    o[b][check[b]][0] = a
    o[b][check[b]][1] = i
    check[a] += 1
    check[b] += 1
for i in range(m)[::-1]:
    visited = [0 for _ in range(n)]
    if dfs(False, i, n):
        result = (result + w[i]) % MOD
        for j in range(n):
            for k in range(check[j]):
                if o[j][k][1] == i:
                    o[j][k][1] = -1
print(result)
