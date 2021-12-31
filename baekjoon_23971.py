from math import ceil
h, w, n, m = map(int, input().split())
print(ceil(h / (n + 1)) * ceil(w / (m + 1)))
