n, m, k = map(int, input().split())
print(((m - 1) + (k - 3) % n + n) % n + 1)
