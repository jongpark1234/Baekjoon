from sys import stdin
from math import acos, atan, sqrt
def calc1(x):
    return pow(x / v, 2) * -4.905 + h + p
def calc2(x):
    return h if x < 0 else h * (1 - pow(x / l, 2) * 2) if x < l / 2 else h * pow(x / l - 1, 2) * 2 if x < l else 0
eps = 1e-50
for _ in range(int(stdin.readline())):
    j, p, h, l = map(int, stdin.readline().split())
    v = max(sqrt(j * 19.62), eps)
    left, right = 0, sqrt((h + p) * pow(v, 2) * 2 / 9.81)
    for i in range(49):
        mid = left + (right - left) / 2
        if calc1(mid) > calc2(mid):
            left = mid
        else:
            right = mid
    result = left + (right - left) / 2
    print(result, max(sqrt((j + p + h - calc2(result)) * 19.62), eps), abs(atan(pow(1 / v, 2) * result * -9.81) - atan(0 if result < 0 else h * result / pow(l, 2) * -4 if result < l / 2 else h * (result / l - 1) / l * 4 if result < l else 0)) * 90 / acos(0))
