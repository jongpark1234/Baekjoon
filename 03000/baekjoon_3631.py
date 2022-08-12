x, y, z, n = map(int, input().split())
for i in range(n):
    print(x * i / n, 0, 0, x * (i + 1) / n, y, z)
