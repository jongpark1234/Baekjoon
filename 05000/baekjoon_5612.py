n = int(input())
m = int(input())
result = m
for _ in range(n):
    a, b = map(int, input().split())
    m += a - b
    result = max(result, m)
    if m < 0:
        print(0)
        break
else:
    print(result)
