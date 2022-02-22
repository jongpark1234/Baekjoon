# pypy3
import sys
sys.setrecursionlimit(10**5)
g = [[] for _ in range(101010)]
sz = [0 for _ in range(101010)]
par = [0 for _ in range(101010)]
def dfs(x, p):
    par[x] = p
    sz[x] = 1
    for i in g[x]:
        if i != p:
            sz[i] += dfs(i, x)
    return sz[x]
ch = [[] for _ in range(101010)]
d = [0 for _ in range(101010)]
chNum = [0 for _ in range(101010)]
chIdx = [0 for _ in range(101010)]
def hld(x, p, num, depth):
    d[x] = depth
    chIdx[x] = len(ch[num])
    chNum[x] = num
    ch[num].append(x)
    go = -1
    for i in g[x]:
        if go == -1 or sz[i] > sz[go]:
            if i != p:
                go = i
    if go != -1:
        hld(go, x, num, depth)
 
    for i in g[x]:
        if i != go and i != p:
            hld(i, x, i, depth + 1)
def getLca(x, y):
    while chNum[x] != chNum[y]:
        if d[x] > d[y]:
            x = par[chNum[x]]
        else:
            y = par[chNum[y]]
    return x if chIdx[x] < chIdx[y] else y
n = int(input())
for nodes in range(n - 1):
    i, j = map(int, input().split())
    g[i].append(j)
    g[j].append(i)
dfs(1, 0)
hld(1, 0, 1, 0)
m = int(input())
for query in range(m):
    i, j = map(int, input().split())
    print(getLca(i, j))