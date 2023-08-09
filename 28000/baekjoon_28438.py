from sys import stdin
n, m, q = map(int, stdin.readline().split())
r = [0 for _ in range(n + 1)]
c = [0 for _ in range(m + 1)]
for _ in range(q):
    b, w, v = map(int, stdin.readline().split())
    if b == 1:
        r[w] += v
    else:
        c[w] += v
for i in range(1, n + 1):
    for j in range(1, m + 1):
        print(r[i] + c[j], end=' ')
    print()
