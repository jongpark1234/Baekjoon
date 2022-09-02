from math import prod
n, m = map(int, input().split())
print(prod([*map(int, input().split())]) % m)
