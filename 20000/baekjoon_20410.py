m, seed, x1, x2 = map(int, input().split())
result1 = result2 = 0
for i in range(m):
    for j in range(m):
        X1, X2 = (i * seed + j) % m, (i * x1 + j) % m
        if X1 == x1 and X2 == x2:
            result1, result2 = i, j
            break
    else:
        continue
    break
print(result1, result2)
