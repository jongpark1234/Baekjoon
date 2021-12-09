from math import ceil
n, a, b, c, d = map(int, input().split())
print(min(ceil(n / a) * b, ceil(n / c) * d))
