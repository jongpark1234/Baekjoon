result = []
a, b = map(int, input().split())
for i in range(-10000, 10001):
    if i ** 2 + 2 * a * i + b == 0:
        result.append(i)
print(*result)
