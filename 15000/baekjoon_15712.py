from sys import setrecursionlimit
setrecursionlimit(10 ** 5)
def f(x: int) -> int:
    if x == 0:
        return 1
    if x == 1:
        return (r + 1) % mod
    if x & 1:
        return f(x >> 1) * (pow(r, (x >> 1) + 1, mod) + 1) % mod
    return (f((x >> 1) - 1) * (pow(r, x >> 1, mod) + 1) % mod + pow(r, x, mod) % mod) % mod
a, r, n, mod = map(int, input().split())
print(a * f(n - 1) % mod)
