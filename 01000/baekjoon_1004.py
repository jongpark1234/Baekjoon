from math import hypot
for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    print(sum((hypot(abs(cx - x1), abs(cy - y1)) < r) ^ (hypot(abs(cx - x2), abs(cy - y2)) < r) for cx, cy, r in [list(map(int, input().split())) for _ in range(int(input()))]))
