def check(n: int, k: int, t: int, speed: int) -> bool:
    numlist = [0] + [x[i] - (speed << 1) * t * i for i in range(1, n + 1)]
    l, r = 1, n
    for i in range(1, k + 1):
        l = i if numlist[i] > numlist[l] else l
    for i in range(k, n + 1):
        r = i if numlist[i] < numlist[r] else r
    ql = qr = k
    vl, vr = numlist[ql], numlist[qr]
    while ql >= l or qr <= r:
        tl, tr = ql, qr
        while qr <= r and vl >= numlist[qr]:
            vr = min(vr, numlist[qr])
            qr += 1
        while ql >= l and vr <= numlist[ql]:
            vl = max(vl, numlist[ql])
            ql -= 1
        if tl == ql and tr == qr:
            return False
    ql, qr = 1, n
    vl, vr = numlist[ql], numlist[qr]
    while ql <= l or qr >= r:
        tl, tr = ql, qr
        while qr >= r and vl >= numlist[qr]:
            vr = min(vr, numlist[qr])
            qr -= 1
        while ql <= l and vr <= numlist[ql]:
            vl = max(vl, numlist[ql])
            ql += 1
        if tl == ql and tr == qr:
            return False
    return True
n, k, t = map(int, input().split())
x = [0] + [int(input()) for _ in range(n)]
l, r = -1, 1000000007
while l < r - 1:
    m = l + r >> 1
    if check(n, k, t, m):
        r = m
    else:
        l = m
print(l + 1)
