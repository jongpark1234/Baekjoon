from math import ceil
a, b, h = map(int, input().split())
print(1 if a >= h else ceil((h - b) / (a - b)))
