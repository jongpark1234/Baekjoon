result = -1
a, b, n, w = map(int, input().split())
for i in range(1, n):
    if a * i + b * (n - i) == w:
        result = i
        for j in range(i + 1, n):
            if a * j + b * (n - j) == w:
                print(-1)
                exit(0)
print(-1 if result == -1 else f'{result} {n - result}')
