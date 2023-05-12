n, k = map(int, input().split())
ret = sum(int(input()) for _ in range(k))
print(*[(ret + (n - k) * i) / n for i in [-3, 3]])
