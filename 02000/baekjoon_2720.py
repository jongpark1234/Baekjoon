from sys import stdin
for _ in range(int(stdin.readline())):
    c = int(stdin.readline())
    q, d, n, p = 0, 0, 0, 0
    while c >= 25:
        c -= 25
        q += 1
    while c >= 10:
        c -= 10
        d += 1
    while c >= 5:
        c -= 5
        n += 1
    while c >= 1:
        c -= 1
        p += 1
    print(q, d, n, p)
