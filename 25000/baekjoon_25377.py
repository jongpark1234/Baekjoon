result = float('inf')
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a <= b:
        result = min(result, b)
print(-1 if result == float('inf') else result)
