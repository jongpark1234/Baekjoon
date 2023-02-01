poslist = [tuple(map(int, input().split())) for _ in range(int(input()))]
Min = float('inf')
x = y = 0
for xi, yi in poslist:
    Max = -float('inf')
    for xj, yj in poslist:
        temp = ((xi - xj) ** 2 + (yj - yi) ** 2) ** 0.5
        Max = max(Max, temp)
    if Max < Min:
        Min = Max
        x, y = xi, yi
print(x, y)
