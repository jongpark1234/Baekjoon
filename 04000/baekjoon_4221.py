from sys import setrecursionlimit
from math import sin, acos, pi
setrecursionlimit(10 ** 4)
def solve(s, e):
    if e - s < 2:
        return 0
    Max = a[s:e + 1].index(max(a[s:e + 1])) + s
    Sum = 0
    for i in range(s, e + 1):
        Sum += a[i]
    result1, result2 = solve(s, Max - 1) + solve(Max + 1, e), 0
    if Sum <= a[Max] * 2:
        return result1
    def trial(x):
        r = 0
        for i in range(s, e + 1):
            r += acos(1 - a[i] * a[i] / (2 * x * x))
        return r
    if trial(a[Max] * 0.5 + 1e-9) < pi * 2:
        left = a[Max] * 0.5 + 1e-9
        right = 1e6
        for _ in range(70):
            mid = (left + right) / 2
            if trial(mid) - 2 * acos(1 - a[Max] * a[Max] / (2 * mid * mid)) < 0:
                left = mid
            else:
                right = mid
        for i in range(s, e + 1):
            ang = acos(1 - a[i] * a[i] / (2 * left * left))
            if Max == i:
                result2 -= 0.5 * left * left * sin(ang)
            else:
                result2 += 0.5 * left * left * sin(ang)
    else:
        left = a[Max] * 0.5
        right = 1e6
        for i in range(70):
            mid = (left + right) / 2
            if trial(mid) < pi * 2:
                right = mid
            else:
                left = mid
        for i in range(s, e + 1):
            ang = acos(1 - a[i] * a[i] / (2 * left * left))
            result2 += 0.5 * left * left * sin(ang)
    return max(result1, result2)
t = 0
while (n := int(input())) != 0:
    t += 1
    a = list(map(int, input().split()))
    print(f'Case {t}: {solve(0, n - 1):.10f}')
