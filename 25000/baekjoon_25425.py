from math import ceil
n, m, a, k = map(int, input().split())
print(*sorted([min(n, a - k + 1), ceil((a - k) / m) + 1], reverse = True))
