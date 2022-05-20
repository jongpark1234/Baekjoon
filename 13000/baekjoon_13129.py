a, b, n = map(int, input().split())
print(*[(a + b) * i + a * (n - i) for i in range(1, n + 1)])
