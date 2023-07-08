result = [0, 0, 0, 0]
for _ in range(int(input())):
    g, c, n = map(int, input().split())
    result[-1 if g == 1 else 0 if c < 3 else c - 2] += 1
print(*result)
