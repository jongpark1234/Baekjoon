n, m, k = map(int, input().split())
print(max(n - m * k, 0), n - m * k + m - 1)
