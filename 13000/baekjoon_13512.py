import sys
sys.setrecursionlimit(10**5)
INF = int(1e9)
seg = [0 for _ in range(404040)]
g = [[] for _ in range(101010)]
par = [0 for _ in range(101010)]
sz = [0 for _ in range(101010)]
c = [0 for _ in range(101010)]
idx = [0 for _ in range(101010)]
ridx = [0 for _ in range(101010)]
ch = [0 for _ in range(101010)]
def update(x, s, e, idx, v):
    if idx < s or e < idx:
        return
    if s != e:
        m = (s + e) // 2
        update(x * 2, s, m, idx, v)
        update(x * 2 + 1, m + 1, e, idx, v)
        seg[x] = min(seg[x * 2], seg[x * 2 + 1])
        return
    seg[x] = v
def getMin(x, l, r, s, e):
    if e < l or r < s:
        return INF
    if l <= s and e <= r:
        return seg[x]
    m = (s + e) // 2
    return min(getMin(x * 2, l, r, s, m), getMin(x * 2 + 1, l, r, m + 1, e))
def dfs(x):
    sz[x] = 1
    for i in g[x]:
        if sz[i] == 0:
            par[i] = x
            dfs(i)
            sz[x] += sz[i]
index = 0
def hld(x):
    global index
    heavy = -1
    index += 1
    idx[x] = index
    ridx[idx[x]] = x
    for i in g[x]:
        if heavy == -1 or sz[i] > sz[heavy]:
            if par[i] == x:
                heavy = i
    if heavy != -1:
        ch[heavy] = ch[x]
        hld(heavy)
    for i in g[x]:
        if par[i] == x and i != heavy:
            ch[i] = i
            hld(i)
def getAns(x):
    ret = INF
    while ch[1] != ch[x]:
        ret = min(ret, getMin(1, idx[ch[x]], idx[x], 1, n))
        x = par[ch[x]]
    ret = min(ret, getMin(1, idx[ch[x]], idx[x], 1, n))
    return ret
n = int(sys.stdin.readline())
for nodes in range(n - 1):
    i, j = map(int, sys.stdin.readline().split())
    g[i].append(j)
    g[j].append(i)
ch[1] = 1
dfs(1)
hld(1)
for i in range(1, n + 1):
    update(1, 1, n, idx[i], INF)
qr = int(sys.stdin.readline())
for query in range(qr):
    i, j = map(int, sys.stdin.readline().split())
    if i == 1:
        c[j] ^= 1
        update(1, 1, n, idx[j], idx[j] if c[j] else INF)
    else:
        ans = getAns(j)
        print(ridx[ans] if ans != INF else -1)