n, x, k = map(int, input().split())
for _ in range(k):
    a, b = map(int, input().split())
    if x in [a, b]:
        x = a + b - x
print(x)
