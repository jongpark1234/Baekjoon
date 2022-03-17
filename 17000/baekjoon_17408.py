from sys import stdin
seg = [[0, 0] for _ in range(404040)]
def init(x, s, e):
    if s == e:
        seg[x] = [a[s - 1], 0]
        return seg[x]
    mid = (s + e) // 2
    tmp = init(x * 2, s, mid) + init(x * 2 + 1, mid + 1, e)
    tmp.sort(reverse=True)
    seg[x] = tmp[:2]
    return seg[x]
def update(x, s, e, idx, v):
    if e < idx or idx < s:
        return seg[x]
    if s == e:
        if s == idx:
            seg[x] = [v, 0]
        return seg[x]
    mid = (s + e) // 2
    tmp = update(x * 2, s, mid, idx, v) + update(x * 2 + 1, mid + 1, e, idx, v)
    tmp.sort(reverse=True)
    seg[x] = tmp[:2]
    return seg[x]
def getAns(x, l, r, s, e):
    if e < l or r < s:
        return [0, 0]
    if l <= s and e <= r:
        return seg[x]
    mid = (s + e) // 2
    tmp = getAns(x * 2, l, r, s, mid) + getAns(x * 2 + 1, l, r, mid + 1, e)
    tmp.sort(reverse=True)
    return tmp[:2]
n = int(stdin.readline())
a = list(map(int, stdin.readline().split())) 
init(1, 1, n)
m = int(stdin.readline())
for query in range(m):
    q, i, j = map(int, stdin.readline().split())
    if q == 1:
        update(1, 1, n, i, j)
    else:
        ret = getAns(1, i, j, 1, n)
        print(ret[0] + ret[1])
