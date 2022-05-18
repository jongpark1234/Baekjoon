from math import log1p
def solve1(x):
    return solve2(x) if x > 1000000 else solve3(x)
def solve2(x):
    return n * log1p(x - 1) + n * 0.57721566490153286060651209008240243104215933593992 + n / (x * 2) - n / (x * x * 12) + n / (x * x * x * x * 120)
def solve3(x):
    ret = 0
    for i in range(1, x + 1):
        ret += n / i
    return ret
def exception():
    ret = 0
    for i in range(n - k + 1, n + 1):
        ret += n / i
    return ret
n, k = map(int, input().split())
if k < 20000000:
    print(exception())
elif k < 10000000000000 and k < n / 10:
    r = 0
    p = n / (n - k) * k
    for i in range(1, 100001):
        r += p / i * (1 if i & 1 else -1)
        p = p * k / (n - k)
        if p == 0:
            break
    print(r + 0.5 - n / ((n - k) * 2) + 1 / (n * 12) - n / (12 * (n - k) ** 2))
print(solve1(n) - solve1(n - k))
