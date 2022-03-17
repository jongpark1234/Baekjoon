import sys
T = int(sys.stdin.readline())
results = []
def recur(start, a, b, c):
    for i in range(start, N):
        a[i + 1] = min(b[i] + 1, c[i] + 1)
        if zone1[i] + zone2[i] <= W: a[i + 1] = min(a[i + 1], a[i] + 1)
        if i > 0 and zone1[i - 1] + zone1[i] <= W and zone2[i - 1] + zone2[i] <= W: a[i + 1] = min(a[i + 1], a[i - 1] + 2)
        if i < N - 1:
            b[i + 1] = a[i + 1] + 1
            if zone1[i + 1] + zone1[i] <= W: b[i + 1] = min(b[i + 1], c[i] + 1)
            c[i + 1] = a[i + 1]+1
            if zone2[i + 1] + zone2[i] <= W: c[i + 1] = min(c[i + 1], b[i] + 1)
    return a, b, c
for _ in range(T):
    N, W = map(int, sys.stdin.readline().split())
    zone1 = list(map(int, sys.stdin.readline().split()))
    zone2 = list(map(int, sys.stdin.readline().split()))
    a = [0 for _ in range(N + 1)]
    b = [0 for _ in range(N + 1)]
    c = [0 for _ in range(N + 1)]
    a[0] = 0
    b[0] = 1
    c[0] = 1
    a, b, c = recur(0, a, b, c)
    res = a[N]
    if N > 1 and zone1[0] + zone1[N - 1] <= W:
        a[1] = 1
        b[1] = 2
        if zone2[0] + zone2[1] <= W:
            c[1] = 1
        else:
            c[1] = 2
        a, b, c = recur(1, a, b, c)
        res = min(res, c[N - 1] + 1)
    if N > 1 and zone2[0] + zone2[N - 1] <= W:
        a[1] = 1
        c[1] = 2
        if zone1[0] + zone1[1] <= W:
            b[1] = 1
        else:
            b[1] = 2
        a, b, c = recur(1, a, b, c)
        res = min(res, b[N - 1] + 1)
    if N > 1 and zone1[0] + zone1[N - 1] <= W and zone2[0] + zone2[N - 1] <= W:
        a[1] = 0
        b[1] = 1
        c[1] = 1
        a, b, c = recur(1, a, b, c)
        res = min(res, a[N - 1] + 2)
    results.append(res)
print('\n'.join(map(str,results)))
