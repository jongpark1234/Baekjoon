n, m, k = map(int, input().split())
fo, fx = m, n - m
bo, bx = k, n - k
print(min(fo, bo) + min(fx, bx))
