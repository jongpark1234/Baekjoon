l, r, a = map(int, input().split())
for i in range(a):
    if l < r:
        l += 1
    else:
        r += 1
print(min(l, r) << 1)
