k, n = map(int, input().split())
print(-1 if n == 1 else (k * n) // (n - 1) + ((k * n) % (n - 1) > 0))
