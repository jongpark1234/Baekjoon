from sys import setrecursionlimit
from math import sin, cos, acos, sqrt
setrecursionlimit(10 ** 5)
def part(h: float, base: float) -> float:
    return dh ** 2 if (dh := h - base) > 0 else 0
def solve(x: float, y: float, h: float) -> None:
    global result
    if 0 <= x < size and 0 <= y < size and hole[x][y]:
        hole[x][y] = False
        if h < 1e-10:
            return
        h = min(h, H)
        result += 1 if a == 0 else part(h, 0) - part(h, cosine) - part(h, sine)
        for i in range(4):
            solve(x + dx[i], y + dy[i], h + dh[i])
n, a = map(int, input().split())
result, size, angle = 0, 0, a * acos(-1) / 180
hole = [[False for _ in range(4096)] for _ in range(4096)]
for i in range(n):
    grid = [[False for _ in range((size << 1) + 1)] for _ in range((size << 1) + 1)]
    for y in range(size):
        for x in range(size):
            grid[y][x + size + 1] = hole[y][x]
            grid[y + size + 1][x + size + 1] = hole[y][x]
            grid[y][x] = not hole[x][y]
            grid[y + size + 1][x] = not hole[x][size - y - 1]
            grid[size][x] = True
    for y in range(len(grid)):
        grid[y][size] = True
    hole = grid
    size = (size << 1) + 1
sine, cosine, H = sin(angle), cos(angle), cos(acos(-1) / 4 - angle) * sqrt(2)
dx, dy, dh = [-1, 1, 0, 0], [0, 0, -1, 1], [sine, -sine, -cosine, cosine]
for i in range(size):
    solve(i, 0, cosine)
print(result if a == 0 else result / cosine / sine / 2)
