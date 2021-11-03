a, b = map(int, input().split())
if a + b < 0 or a - b < 0  or (a + b) % 2:
    print(-1)
else:
    x = (a + b) // 2; y = a - x
    print(max(x, y), min(x, y))