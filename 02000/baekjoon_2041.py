n, m = map(int, input().split())
grid = [[0 for _ in range(m)] for _ in range(n)]
f = 1
p = 0
grid[0][0] = n * m
for i in range(1, n + m - 1):
    f *= -1
    for j in range(max(0, i - m + 1), min(n - 1, i) + 1):
        p += (i > j > 0) + 1
        if i == j:
            grid[j][i - j] = grid[i - 1][i - j] + p * f
        else:
            grid[j][i - j] = grid[j][i - j - 1] + p * f
for i in grid:
    print(*i)
