x, y = map(int, input().split())
result = 1000 * x / y
for _ in range(int(input())):
    a, b = map(int, input().split())
    result = min(result, 1000 * a / b)
print(result)
