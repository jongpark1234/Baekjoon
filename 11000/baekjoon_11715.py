from sys import stdin
from bisect import bisect_right
def indexing(l, r):
    return (l + r) | (l != r)
def cmp(a, b):
	if a == n or b == n:
		return a + b - n
	else:
		return [b, a][hpdp[a][1] < hpdp[b][1]]
def init(left, right):
    if left == right:
        numarr[indexing(left, right)] = left
        return
    mid = left + right >> 1
    init(left, mid)
    init(mid + 1, right)
    numarr[indexing(left, right)] = cmp(numarr[indexing(left, mid)], numarr[indexing(mid + 1, right)])
def query(left, right, a, b):
    if a <= left and right <= b:
        return numarr[indexing(left, right)]
    mid = left + right >> 1
    if b <= mid:
        return query(left, mid, a, b)
    elif a > mid:
        return query(mid + 1, right, a, b)
    else:
        return cmp(query(left, mid, a, b), query(mid + 1, right, a, b))
def erase(left, right, pos):
    if left == right:
        numarr[indexing(left, right)] = n
        return
    mid = left + right >> 1
    if pos <= mid:
        erase(left, mid, pos)
    else:
        erase(mid + 1, right, pos)
    numarr[indexing(left, right)] = cmp(numarr[indexing(left, mid)], numarr[indexing(mid + 1, right)])
def erasing(x):
    global result
    erased[x] = True
    result += 1
    erase(0, n - 1, x)
def getHP():
    global idx
    while idx < n and erased[idx]:
        idx += 1
    return idx
def getDP(x):
    return query(0, n - 1, 0, bisect_right(hpdp, [x + 1, -1]) - 1)
def solve():
    global idx, breaked
    numlist = []
    hp = getHP()
    if hp == n:
        return False
    dp = getDP(hpdp[hp][0] + c)
    if hpdp[hp][1] > hpdp[dp][1]:
        temp = hpdp[dp][1]
        while True:
            numlist.append(dp)
            erasing(dp)
            dp = getDP(hpdp[hp][0] + c)
            if hpdp[dp][1] != temp:
                break
    else:
        numlist.append(hp)
        erasing(hp)
    for i in numlist:
        x = i
        while idx < n and hpdp[idx][0] < hpdp[x][0] - c:
            if not erased[idx]:
                numlist.append(idx)
                erasing(idx)
            idx += 1
        while True:
            dp = getDP(hpdp[x][0] + c)
            if dp == n or hpdp[dp][1] >= hpdp[x][1]:
                break
            numlist.append(dp)
            erasing(dp)
    for i in numlist:
        x = i
        if isblocking[x]:
            breaked = True
        dp = getDP(hpdp[x][0] + c)
        if dp == n or hpdp[dp][1] > hpdp[x][1]:
            breaked = True
        else:
            isblocking[dp] = True
    return not breaked
idx = result = 0
numarr = [0 for _ in range(100001)]
erased = [False for _ in range(50001)]
isblocking = [False for _ in range(50001)]
breaked = False
n, c = map(int, stdin.readline().split())
hpdp = sorted([list(map(int, stdin.readline().split())) for _ in range(n)])
init(0, n - 1)
while solve():
    pass
print(result)
