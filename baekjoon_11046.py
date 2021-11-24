import itertools as I, sys
def manacher(s):
    n = len(s)
    *a, r, p = [0] * (n + 2)
    for i in range(n):
        if i <= r:
            a[i] = min(a[2 * p - i], r - i)
        else:
            a[i] = 0
        while i - a[i] - 1 >= 0 and i + a[i] + 1 < n and s[i - a[i] - 1] == s[i + a[i] + 1]:
            a[i] += 1
        if r < i + a[i]:
            r, p = i + a[i], i
    return a
input()
g = lambda: [*map(int, sys.stdin.readline().split())]
l = g()
v = [*I.chain(*[[i, 0] for i in l])]
v.pop()
a = manacher(l)
b = manacher(v)[1::2]
for i in range(int(input())):
    v, e = g()
    l, w = e - v + 1,0
    if l & 1:
        x = 1 + a[(e + v) // 2 - 1] * 2
    else:
        x = (b[(e + v) // 2 - 1] + 1) // 2 * 2
    print(int(x >= l))
