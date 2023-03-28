x, n = map(int, input().split())
for i in range(n):
    x = x << 1 ^ 6 if x & 1 else x >> 1 ^ 6
print(x)
