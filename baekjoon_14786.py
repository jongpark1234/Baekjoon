from math import sin
a, b, c = map(int, input().split())
l, r, x = 0, 200000, 0
while r - l > 1e-9:
    x = (l + r) / 2
    if a * x + b * sin(x) < c:
        l = x - 1e-10
    else:
        r = x + 1e-10
print(x)
