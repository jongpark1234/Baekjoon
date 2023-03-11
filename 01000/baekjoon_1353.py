from math import e
s, p = map(int, input().split())
if s == p:
    print(1)
else:
    i, prv = 2, -1
    while True:
        cur = pow(s / i, i)
        if prv > cur:
            print(-1)
            break
        if p <= cur:
            print(i)
            break
        i += 1
        prv = cur
