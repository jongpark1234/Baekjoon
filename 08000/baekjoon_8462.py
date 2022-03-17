# pypy3
from sys import stdin
c = [0 for _ in range(1000001)]
def add(x):
    global res
    c[x] += 1
    res += (c[x] * 2 - 1) * x
def erase(x):
    global res
    c[x] -= 1
    res -= (c[x] * 2 + 1) * x
n, qr = map(int, stdin.readline().split())
a = [0] + list(map(int, stdin.readline().split()))
q = []
for i in range(qr):
    x, y = map(int, stdin.readline().split())
    q.append((i, x, y))
sqrtN = int(n ** 0.5)
q.sort(key=lambda x:(x[1]//sqrtN, x[2]))
ans = [0 for _ in range(qr)]
res = 0
s = 0
e = 0
for i in range(qr):
    while s < q[i][1]: erase(a[s]); s += 1
    while s > q[i][1]: s -= 1; add(a[s])
    while e > q[i][2]: erase(a[e]); e -= 1
    while e < q[i][2]: e += 1; add(a[e])
    ans[q[i][0]] = res
print(*ans, sep='\n')
