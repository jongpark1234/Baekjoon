def Round(x):
    return int(x) + (1 if x - int(x) >= 0.5 else 0)
for _ in range(int(input())):
    r, g, b = 0, 0, 0
    for _ in range(10):
        x, y, z = map(int, input().split())
        r += x
        g += y
        b += z
    print(Round(r / 10), Round(g / 10), Round(b / 10))
