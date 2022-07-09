from math import comb
n, k = map(int, input().split())
a = list(map(int, input().split()))
print(comb(n, k) * (1 << k - 1) % 1000000007)
