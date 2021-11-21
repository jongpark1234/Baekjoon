a, b = map(int, input().split())
print(len(range(min(a, b) + 1, max(a, b))))
for i in range(min(a, b) + 1, max(a, b)):
    print(i, end=' ')
