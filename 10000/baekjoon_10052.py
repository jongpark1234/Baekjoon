from math import floor, ceil
coord = []
lo, hi, m = 1e9, -1e9, 1e-7
def ccw(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
def cross(p, q):
    return ((p[0] - p[2]) * (-(q[3] - q[1]) * q[0] - (q[0] - q[2]) * q[1]) - (-(p[3] - p[1]) * p[0] - (p[0] - p[2]) * p[1]) * (q[0] - q[2])) / ((p[3] - p[1]) * (q[0] - q[2]) - (p[0] - p[2]) * (q[3] - q[1]))
def calc(a, b, c):
    return cross([a[0] * 2, a[1] * 2, b[0] + c[0], b[1] + c[1]], [b[0] * 2, b[1] * 2, a[0] + c[0], a[1] + c[1]]) / 2 if ccw(a, b, c) else 0
n = int(input())
for i in range(n):
    coord.append(list(map(int, input().split())))
    if coord[i][1] == 0:
        lo = min(lo, coord[i][0])
        hi = max(hi, coord[i][0])
p = coord[0][0]
g = s = 0
for i in range(1, n - 1):
    value = ccw(coord[0], coord[i], coord[i + 1])
    s += value
    g += calc(coord[0], coord[i], coord[i + 1]) * value / 2
if s < 0:
    s *= -1
    g *= -1
s /= 2
g /= s
left, right = 1e-2, 1e18
if abs(lo - p) <= m:
    if g - lo < -m:
        print('unstable')
        exit(0)
else:
    if lo - p < 0:
        left = max(left, (g - lo) * s / (lo - p))
    else:
        right = min(right, (g - lo) * s / (lo - p))
if abs(hi - p) <= 1e-8:
    if hi - g < -1e-8:
        print('unstable')
        exit(0)
else:
    if hi > p:
        left = max(left, (g - hi) * s / (hi - p))
    else:
        right = min(right, (g - hi) * s / (hi - p))
if left > right:
    print('unstable')
    exit(0)
print(floor(left + m), '..', 'inf' if right > 1e17 else ceil(right - m))
