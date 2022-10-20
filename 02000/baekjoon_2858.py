r, b = map(int, input().split())
p, q = r + 4 >> 1, r + b
for i in range(1, p + 1):
    j = p - i
    if i * j == q:
        print(j, i)
        break
