result = 0
plain = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1 - 1, x2 - 1):
        for j in range(y1 - 1, y2 - 1):
            plain[i][j] = 1
for i in plain:
    result += sum(i)
print(result)
