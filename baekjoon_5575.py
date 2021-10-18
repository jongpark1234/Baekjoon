from sys import *
for i in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, stdin.readline().split())
    if s1 > s2:
        m2 -= 1
        s2 += 60
    s = s2 - s1
    if m1 > m2:
        h2 -= 1
        m2 += 60
    m = m2 - m1
    h = h2 - h1
    print(h, m, s)